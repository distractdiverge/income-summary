import os
import pdfplumber
import re
import datetime
import json
from collections import defaultdict

def extract_transactions_from_pdf(file_path):
    transactions = []
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                parsed_text = parse_transactions(text)
                transactions.extend(parsed_text)

    return transactions

def parse_statement_date(text):
    from_regex = r"(?P<from>\d{2}/\d{2}/\d{4})"
    to_regex = r"(?P<to>\d{2}/\d{2}/\d{4})"
    date_regex = re.compile(fr"For the period\s+{from_regex}\s+to\s+{to_regex}.*")

    match = date_regex.search(text)
    if match:
        from_date_str, to_date_str = match.groups()
        from_date = datetime.datetime.strptime(from_date_str, "%m/%d/%Y")
        to_date = datetime.datetime.strptime(to_date_str, "%m/%d/%Y")
        return (from_date, to_date)
    else:
        return None

###
### Should this transaction be processed furter?
### There are certain transactions that match the general txn regex, 
### but really, they're aggregated data, so this fn contains some patterns to exclude
### and then returns true/false
###
def should_process_transaction(text):
    date_value_pattern = re.compile(r"(\d{2}/\d{2}\s+[\d,]+\.\d{2}\s+){2,}")

    if date_value_pattern.search(text):
        return False
    
    return True # Yes, process by default

def parse_transaction(text, statement_from_date = None, statement_to_date = None):
    ###
    ### Parse a SINGLE transaction and return its parts
    ###
    # Possible 'TXN Type' Categories (extracted from examples)
    # "XXXX Debit Card Purchase", 
    # "POS Purchase",
    # "Card Free ATM W/D"
    # "ATM Withdrawal"
    # "XXXX Recurring Debit Card",
    # International POS Fee 

    # Example Line to match: 01/17 30.00 XXXX Debit Card Purchase Paypal *Add To Bal
    date_regex = r"(?P<date>\d{2}/\d{2})"
    amount_regex = r"(?P<amount>[\d,]{0,}\.\d{2})"
    desc_regex = r"(?P<description>.+)"
    transaction_pattern = re.compile(fr"{date_regex}\s+{amount_regex}\s+{desc_regex}")
    match = transaction_pattern.search(text.strip())

    txn_year = None
    ## TODO: if from/to dates are not None, use them to add the year to the date_obj for this txn
    if statement_from_date is not None and statement_to_date is not None:
        if statement_from_date.year == statement_to_date.year:
            txn_year = statement_from_date.year
        else:
            print(f"Statement From({statement_from_date.year})/To({statement_to_date.year}) dates have diff years")
            # This case should ONLY occur for a January statement, so we can assume Jan (to-year) & Feb (from-year)

    
    should_process = should_process_transaction(text)

    if match and should_process:
        date_str, amount, description = match.groups()
        date_obj = datetime.datetime.now()
        
        if date_str.startswith("01"): # TODO: Needs more testing
            date_obj = datetime.datetime.strptime(f"{date_str}/{statement_to_date.year}", "%m/%d/%Y")
        else:
            date_obj = datetime.datetime.strptime(f"{date_str}/{statement_from_date.year}", "%m/%d/%Y")

        amount_value = float(amount.replace(",",""))

        return (date_obj, amount_value, description)
    else:
        print(f"Could not match: '{text}'")
    
    return None

def parse_transactions(text):
    transactions = []
    lines = text.split("\n")

    # TODO: Parse out the line that indicates the Date Range (to get the Year)
    # line example: 'For the period 03/06/2024 to 04/03/2024 Number of enclosures: 0'

    statement_from_date = None
    statement_to_date = None

    for line in lines:
        
        transaction = parse_transaction(line, statement_from_date, statement_to_date)
        
        if transaction is not None:
            (date_str, amount_value, description) = transaction
            transactions.append((date_str, description, amount_value))
        elif "for the period" in line.lower():
            dates = parse_statement_date(line)
            statement_from_date, statement_to_date = dates
            
    return transactions

def aggregate_income_by_month(transactions):
    return transactions

def save_summary(income_summary, file_path="income_summary.json"):
    with open(file_path, "w") as json_file:
        json.dump(income_summary, json_file, default=str, indent=4)
    
    print("Income Summary saved as " + file_path)


def process_statement(file_path):
    print("Processing Statement " + file_path)
    transactions = extract_transactions_from_pdf(file_path)
    return transactions


def process_statements(directory):
    all_transactions = []

    for file in os.listdir(directory):
        if file.endswith(".pdf"):
            transactions = process_statement(os.path.join(directory, file))
            all_transactions.extend(transactions)
    
    income_summary = aggregate_income_by_month(all_transactions)
    save_summary(income_summary)


if __name__ == "__main__":
    statements_directory = "./data/"
    process_statements(statements_directory)

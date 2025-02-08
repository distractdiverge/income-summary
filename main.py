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
                print(json.dumps(parsed_text))
                transactions.extend(parsed_text)

    return transactions

def parse_transaction(text):
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

    if match:
        date_str, amount, description = match.groups()
            
        # date_obj = datetime.datetime.strptime(f"{date_str}/{cuurent_year}")
        # date_obj = datetime.datetime.now()

        # amount_value = float(amount.replace(",",""))

        return (date_str, amount, description)
    else:
        print(f"Could not match: '{text}'")
    
    return None



def parse_transactions(text):
    transactions = []
    lines = text.split("\n")

    for line in lines:
        transaction = parse_transaction(line)
        
        if transaction is not None:
            (date_str, amount_value, description) = transaction
            transactions.append((date_str, description, amount_value))
            
    return transactions

def aggregate_income_by_month(transactions):
    pass

def save_summary(income_summary, file_path="income_summary.json"):
    with open(file_path, "w") as json_file:
        json.dump(income_summary, json_file, indent=4)
    
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

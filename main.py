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

def parse_transactions(text):
    transactions = []
    lines = text.split("\n")
    print(len(lines), " Lines")

    # Possible 'TXN Type' Categories (extracted from examples)
    # "XXXX Debit Card Purchase", 
    # "POS Purchase",
    # "Card Free ATM W/D"
    # "ATM Withdrawal"
    # "XXXX Recurring Debit Card",
    # International POS Fee 

    # Example Line to match: 01/17 30.00 XXXX Debit Card Purchase Paypal *Add To Bal
    transaction_pattern = re.compile(r"(\d{2}/\d{2})\s+([\d,]+\.\d{2})\s+(.+)")

    for line in lines:
        match = transaction_pattern.search(line.strip())
        if "deposit" in line.lower():
            print(f"{repr(line)}")
        
        if match:
            #print("matched")
            date_str, amount, description = match.groups()
            
            # date_obj = datetime.datetime.strptime(f"{date_str}/{cuurent_year}")
            date_obj = datetime.datetime.now()

            amount_value = float(amount.replace(",",""))

            #print(f"Processing TXN: {date_str}, {amount}, {description}")

            #if any(keyword in description.lower() for keyword in ["deposit", "ach credit", "direct deposit"]):
            if amount_value > float(1000.00):
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
    
    print(f"{repr(all_transactions)}")
    income_summary = aggregate_income_by_month(all_transactions)
    save_summary(income_summary)


if __name__ == "__main__":
    statements_directory = "./data/"
    process_statements(statements_directory)

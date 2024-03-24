"""
Personal Finance Manager (PFM) - Final Project Solution

This simplified version includes basic functionalities: recording transactions, viewing them,
and summarizing finances.
"""

import csv
from datetime import datetime


# File to store transaction data
TRANSACTION_FILE = 'transactions.csv'


def record_transaction():
    """Records a new transaction to the file."""
    amount = input("Enter the amount: ")
    category = input("Enter the category: ")
    transaction_type = input("Enter the type (income/expense): ")
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(TRANSACTION_FILE, 'a', newline = '') as file:
        writer = csv.writer(file)
        writer.writerow([date, transaction_type, category, amount])


def view_transactions():
    """Displays all transactions."""
    try:
        with open(TRANSACTION_FILE, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("No transactions found.")


def summarize_finances():
    """Provides a summary of total income, expenses, and net savings."""
    total_income = 0
    total_expense = 0
    try:
        with open(TRANSACTION_FILE, 'r') as file:
            reader = csv.reader(file)
            for date, transaction_type, category, amount in reader:
                if transaction_type.lower() == 'income':
                    total_income += float(amount)
                elif transaction_type.lower() == 'expense':
                    total_expense += float(amount)
    except FileNotFoundError:
        print("No transactions found to summarize.")

    net_savings = total_income - total_expense
    print(
        f"Total Income: {total_income}, Total Expense: {total_expense}, Net Savings: {net_savings}")


def main():
    """Main function to run the PFM program."""
    while True:
        print("\nPersonal Finance Manager")
        print("1. Record a Transaction")
        print("2. View Transactions")
        print("3. Summarize Finances")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            record_transaction()
        elif choice == '2':
            view_transactions()
        elif choice == '3':
            summarize_finances()
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid option, please try again.")


if __name__ == "__main__":
    main()

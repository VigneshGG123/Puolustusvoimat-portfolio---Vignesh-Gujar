import os
import json
from datetime import datetime, timedelta

file_name = "expense_data.json"

def load_data():
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            return json.load(file)
    else:
        return {'transactions': []}

def save_data(data):
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=2)

def add_income(data):
    amount = float(input("Enter income amount: "))
    source = input("Enter income source: ")

    transaction = {'type': 'income', 'amount': amount, 'source': source, 'date': (datetime.now() + timedelta(hours=2)).strftime('%Y-%m-%d %H:%M')}
    data['transactions'].append(transaction)
    save_data(data)
    print("Income added successfully!")

def add_expense(data):
    amount = float(input("Enter expense amount: "))
    category = input("Enter expense category: ")

    transaction = {'type': 'expense', 'amount': amount, 'category': category, 'date': (datetime.now() + timedelta(hours=2)).strftime('%Y-%m-%d %H:%M')}
    data['transactions'].append(transaction)
    save_data(data)
    print("Expense added successfully!")

def edit_transaction(data):
    while True:
        if not data['transactions']:
            print("No transactions to edit.")
            return

        view_transactions(data)

        try:
            print("\nEdit Transaction Menu:")
            print("1. Choose a transaction to edit")
            print("2. Exit")

            choice = input("Enter your choice (1-2): ")

            if choice == "1":
                index = int(input("Enter the transaction index to edit: ")) - 1

                if 0 <= index < len(data['transactions']):
                    transaction = data['transactions'][index]

                    update_amount = input("Do you want to update the amount? (yes/no): ")
                    update_description = input("Do you want to update the description? (yes/no): ")

                    if update_amount.lower() == 'yes':
                        new_amount = float(input("Enter new amount: ") or transaction['amount'])
                        transaction['amount'] = new_amount

                    if update_description.lower() == 'yes':
                        new_description = input("Enter new description: ") or transaction.get('source' if transaction['type'] == 'income' else 'category', '')
                        if transaction['type'] == 'income':
                            transaction['source'] = new_description
                        else:
                            transaction['category'] = new_description

                    transaction['date'] = (datetime.now() + timedelta(hours=2)).strftime('%Y-%m-%d %H:%M')

                    save_data(data)
                    print("Transaction edited successfully!")
                else:
                    print("Invalid index.")
            elif choice == "2":
                print("Exiting Edit Transaction. Returning to main menu.")
                break
            else:
                print("Invalid choice. Please enter 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter a valid index.")

def view_transactions(data):
    transactions = data['transactions']

    if not transactions:
        print("No transactions to display.")
    else:
        print("\nTransactions:")
        for i, transaction in enumerate(transactions, start=1):
            print(f"{i}. {transaction['date']} - {transaction['type'].capitalize()}: {transaction.get('source' if transaction['type'] == 'income' else 'category', '')} "
                  f"(${transaction['amount']})")

def view_balance(data):
    transactions = data['transactions']
    balance = sum(transaction['amount'] if transaction['type'] == 'income' else -transaction['amount'] for transaction in transactions)

    print(f"\nCurrent Balance: ${balance:.2f}")

def main():
    print("Expense Tracker\n")
    data = load_data()

    while True:
        print("\nMain Menu:")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Edit Transaction")
        print("4. View Transactions")
        print("5. View Balance")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_income(data)
        elif choice == "2":
            add_expense(data)
        elif choice == "3":
            edit_transaction(data)
        elif choice == "4":
            view_transactions(data)
        elif choice == "5":
            view_balance(data)
        elif choice == "6":
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()

# Simple Bank Account Management System

# Class to represent a bank account
class BankAccount:
    def __init__(self, account_holder_name, account_number, initial_balance=0):
        self.account_holder_name = account_holder_name
        self.account_number = account_number
        self.balance = initial_balance

    # Method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully. New balance: ₹{self.balance}")
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    # Method to withdraw money
    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Insufficient balance. Current balance: ₹{self.balance}")
        elif amount <= 0:
            print("Invalid withdrawal amount. Please enter a positive value.")
        else:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully. New balance: ₹{self.balance}")

    # Method to check balance
    def check_balance(self):
        print(f"Account balance: ₹{self.balance}")

# Bank system to manage multiple accounts
class BankSystem:
    def __init__(self):
        self.accounts = {}

    # Create a new bank account
    def create_account(self):
        account_holder_name = input("Enter account holder's name: ")
        account_number = input("Enter account number: ")
        initial_balance = float(input("Enter initial deposit amount: "))

        if account_number in self.accounts:
            print("Account number already exists. Please use a different account number.")
        else:
            new_account = BankAccount(account_holder_name, account_number, initial_balance)
            self.accounts[account_number] = new_account
            print(f"Account created successfully for {account_holder_name} with balance ₹{initial_balance}")

    # Access an account by account number
    def access_account(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number]
        else:
            print("Account not found. Please check the account number.")
            return None

# Main menu to operate the bank system
def main_menu(bank_system):
    while True:
        print("\nBank Account Management System")
        print("1. Create New Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Account Balance")
        print("5. Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            bank_system.create_account()

        elif choice == '2':
            account_number = input("Enter account number: ")
            account = bank_system.access_account(account_number)
            if account:
                amount = float(input("Enter deposit amount: "))
                account.deposit(amount)

        elif choice == '3':
            account_number = input("Enter account number: ")
            account = bank_system.access_account(account_number)
            if account:
                amount = float(input("Enter withdrawal amount: "))
                account.withdraw(amount)

        elif choice == '4':
            account_number = input("Enter account number: ")
            account = bank_system.access_account(account_number)
            if account:
                account.check_balance()

        elif choice == '5':
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")

# Run the bank system
if __name__ == "__main__":
    bank_system = BankSystem()
    main_menu(bank_system)

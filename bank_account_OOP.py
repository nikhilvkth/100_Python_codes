import random

class BankAccount:
    def __init__(self, account_holder, initial_balance):
        self.account_holder = account_holder
        self.balance = initial_balance
        self.account_number = self.generate_account_number()

    def generate_account_number(self):
        # Generating a random 8-digit account number
        return random.randint(10000000, 99999999)

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds. Withdrawal canceled.")

    def get_balance(self):
        return self.balance

# Example Usage
account_holder_name = "John Doe"
initial_balance = 1000

# Creating a BankAccount instance
account = BankAccount(account_holder_name, initial_balance)

# Performing transactions
account.deposit(500)
account.withdraw(200)
account.withdraw(1000)  # Attempting to withdraw more than the balance

# Displaying the final balance
final_balance = account.get_balance()
print(f"\nFinal balance for {account.account_holder}'s account: ${final_balance}")

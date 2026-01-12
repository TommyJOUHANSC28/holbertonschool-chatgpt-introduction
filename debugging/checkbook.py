#!/usr/bin/python3
class Checkbook:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount
        if amount <= 0:
            print("The amount must be positive.")
            return
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        if amount <= 0:
            print("The amount must be positive.")
            return
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        print("Current Balance: ${:.2f}".format(self.balance))

def ask_amount(message):
    """Request an amount while securing user input"""
    while True:
        try:
            amount = float(input(message))
            return amount
        except ValueError:
            print("❌ Error: Please enter a valid number.")

def main():
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").lower()
        if action == 'exit':
            print("Bye !")
            break
        elif action == 'deposit':
            amount = ask_amount(input("Enter the amount to deposit: $"))
            cb.deposit(amount)
        elif action == 'withdraw':
            amount = ask_amount(input("Enter the amount to withdraw: $"))
            cb.withdraw(amount)
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()

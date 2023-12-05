class BankAccount:
    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient balance"
        self.balance -= amount
        return self.balance

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account: {self.account_number}, Name: {self.name}, Balance: {self.balance}"

from bank_account import BankAccount

def main():
    # Create bank accounts
    accounts = {}
    accounts["123"] = BankAccount("123", "John Doe")
    accounts["456"] = BankAccount("456", "Jane Doe")

    # Simulate bank operations
    print(accounts["123"])
    accounts["123"].deposit(1000)
    print(accounts["123"])
    print(accounts["123"].withdraw(500))
    print(accounts["123"])

    print(accounts["456"])
    accounts["456"].deposit(2000)
    print(accounts["456"])
    print(accounts["456"].withdraw(2500))
    print(accounts["456"])

if __name__ == "__main__":
    main()

```python
# database.py

import sqlite3

class Database:
    def __init__(self, db_name="bank.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        try:
            self.conn.execute('''CREATE TABLE accounts
                                 (account_number TEXT PRIMARY KEY,
                                  name TEXT,
                                  balance REAL);''')
        except sqlite3.OperationalError:
            # Table already exists
            pass

    def add_account(self, account_number, name, balance):
        self.conn.execute("INSERT INTO accounts VALUES (?, ?, ?)", 
                          (account_number, name, balance))
        self.conn.commit()

    def update_balance(self, account_number, balance):
        self.conn.execute("UPDATE accounts SET balance = ? WHERE account_number = ?",
                          (balance, account_number))
        self.conn.commit()

    def get_account(self, account_number):
        cursor = self.conn.execute("SELECT * FROM accounts WHERE account_number = ?", 
                                   (account_number,))
        return cursor.fetchone()

    def close(self):
        self.conn.close()
```

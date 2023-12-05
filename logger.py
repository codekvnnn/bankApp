import logging

logging.basicConfig(filename='bank.log', level=logging.INFO)

def log_transaction(account_number, transaction_type, amount, status):
    logging.info(f"Account: {account_number}, Transaction: {transaction_type}, Amount: {amount}, Status: {status}")
```

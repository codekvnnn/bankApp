class Auth:
    def __init__(self, user_data):
        self.user_data = user_data  # This could be a database or a dictionary

    def validate_login(self, account_number, password):
        user = self.user_data.get_account(account_number)
        if user and user['password'] == password:
            return True
        return False
```

# BankAccount Class

The `BankAccount` class in Python is designed to represent bank accounts, allowing users to perform various banking operations. The class includes attributes for balance, interest rate, and an account name.

## Class Attributes:

- `accounts`: A class-level attribute that stores a list of all bank accounts created.

## Class Constructor:

```python
def __init__(self, account_name, int_rate, balance=0):
```

- `account_name`: A string representing the name of the bank account.
- `int_rate`: A decimal value representing the interest rate (e.g., 0.05 for 5%).
- `balance` (Optional, default: 0): The initial balance of the account. If not provided, it starts at $0.

## Class Methods:

- **`deposit(self, amount)`**: This method allows users to deposit money into their bank account. It increases the account balance by the given `amount` and returns the updated `BankAccount` instance.

- **`withdraw(self, amount)`**
Users can withdraw money from their bank account using this method. It decreases the account balance by the given `amount` if sufficient funds are available. If not, it charges a $5 fee and prints a message. It returns the updated `BankAccount` instance.

- **`display_account_info(self)`**: This method displays the account name and current balance to the console. It returns the `BankAccount` instance.

- **`yield_interest(self)`**: To simulate interest accrual, this method increases the account balance based on the current balance and the interest rate. It returns the updated `BankAccount` instance.

- **`display_all_accounts(cls)`**: A class method that displays the account information for all `BankAccount` instances created.

## Example Usage:

```python
# Creating a Checking Account
checking = BankAccount("Checking", 0.2, 1000)
checking.deposit(850).deposit(455).deposit(100).withdraw(700).yield_interest().display_account_info()

# Creating a Savings Account
savings = BankAccount("Savings", 0.075, 4500)
savings.display_account_info().deposit(90).deposit(180).withdraw(45).deposit(270).deposit(360).withdraw(225).yield_interest().display_account_info()

# Displaying All Accounts
BankAccount.display_all_accounts()
```

In this example, we create instances of `BankAccount`, perform various transactions, and demonstrate the use of class methods.

The `BankAccount` class provides a basic framework for managing bank accounts and can be extended or customized as needed in a real-world banking application.

---
<p align="right">Completed: ２０２３年１０月０５日（木）</p>
# Users with Bank Accounts

This repository contains two Python class files: `BankAccount.py` and `User.py`. These classes are designed to simulate a simple banking system with basic account management features.

## BankAccount Class

The `BankAccount` class represents a bank account and includes the following attributes and methods:

### Attributes:

- `accounts`: A class-level attribute that stores all instances of the `BankAccount` class.
- `interest_rate`: The interest rate for the account.
- `balance`: The current balance of the account.

### Methods:

- `__init__(self, interest_rate, balance)`: Initializes a new bank account with the given interest rate and initial balance.
- `deposit(self, amount)`: Deposits a specified amount into the account.
- `withdraw(self, amount)`: Withdraws a specified amount from the account, with appropriate error handling for insufficient funds.
- `display_account_info(self)`: Displays the current balance of the account.
- `yield_interest(self)`: Applies interest to the account balance.
- `display_all_accounts(cls)`: Class method to display information for all accounts created.

## User Class

The `User` class represents a bank user and includes the following attributes and methods:

### Attributes:

- `first_name`: The user's first name.
- `last_name`: The user's last name.
- `email`: The user's email address.
- `account`: An instance of the `BankAccount` class for the user's primary checking account.
- `accounts`: A dictionary to store additional user accounts.

### Methods:

- `__init__(self, first_name, last_name, email)`: Initializes a new user with the given first name, last name, and email.
- `display_full_name(self)`: Returns the user's full name.
- `create_account(self, interest_rate=0.1, balance=0, account_name='checking')`: Creates a new account for the user.
- `make_deposit(self, deposited_amount, account_name='checking')`: Makes a deposit into the specified account.
- `make_withdrawal(self, withdrawal_amount, account_name='checking')`: Makes a withdrawal from the specified account.
- `display_user_balance(self, account_name='checking')`: Displays the balances of all user accounts.
- `transfer_money(self, source_account, target_account, amount_to_transfer, other_user=None)`: Transfers money between user accounts with various authorization checks.

### Example Usage of Transferring Between Accounts

#### Transferring Between Checking Accounts

```python
print("== Transferring between checking accounts ==".upper())
jdoe.transfer_money('checking', 'checking', 50, jsmithy)
jdoe.transfer_money('savings', 'checking', 25)
jdoe.transfer_money('checking', 'savings', 25)
jdoe.display_user_balance()
```

In this section, the example demonstrates transferring money between different checking accounts and between checking and savings accounts owned by the same user (`jdoe`). Here's how it works:

- `jdoe.transfer_money('checking', 'checking', 50, jsmithy)`: This line transfers $50 from Jane Doe's checking account to John Smith's checking account (`jsmithy`). Since they are different users, this transfer is allowed.

- `jdoe.transfer_money('savings', 'checking', 25)`: This line transfers $25 from Jane Doe's savings account to her checking account. This is allowed since it's within the same user's accounts.

- `jdoe.transfer_money('checking', 'savings', 25)`: This line attempts to transfer $25 from Jane Doe's checking account to her savings account. This is also allowed as it's within the same user's accounts.

- `jdoe.display_user_balance()`: Finally, this line displays the balances of all Jane Doe's accounts, including both checking and savings.

#### Transferring Between Checking & Savings Accounts

```python
print("== Transferring between checking & savings accounts ==".upper())
jsmithy.display_user_balance()
jsmithy.transfer_money('checking', 'savings', 15, jdoe)
jdoe.transfer_money('savings', 'savings', 15, jsmithy)
```

In this section, the example demonstrates transferring money between checking and savings accounts. Here's how it works:

- `jsmithy.display_user_balance()`: This line displays John Smith's account balances, which initially only includes a checking account.

- `jsmithy.transfer_money('checking', 'savings', 15, jdoe)`: This line attempts to transfer $15 from John Smith's checking account to his non-existent savings account. Since there's no savings account for John Smith, this transfer is unsupported, and an error message will be displayed.

- `jdoe.transfer_money('savings', 'savings', 15, jsmithy)`: This line attempts to transfer $15 from Jane Doe's savings account to John Smith's savings account. However, this action is unauthorized because savings accounts cannot be transferred between users, as indicated in the logic of the `transfer_money()` method.

#### Transferring Between a User's Own Accounts

```python
print("== Transferring between own accounts ==".upper())
jdoe.display_user_balance()
jdoe.transfer_money('savings', 'checking', 10)
jdoe.transfer_money('checking', 'savings', 25)
```

In this section, the example demonstrates transferring money between Jane Doe's own accounts. Here's how it works:

- `jdoe.display_user_balance()`: This line initially displays the balances of Jane Doe's accounts.

- `jdoe.transfer_money('savings', 'checking', 10)`: This line attempts to transfer $10 from Jane Doe's savings account to her checking account. Since it's an authorized transfer within the same user's accounts, it is allowed.

- `jdoe.transfer_money('checking', 'savings', 25)`: This line attempts to transfer $25 from Jane Doe's checking account to her savings account. Again, it's an authorized transfer within the same user's accounts and is allowed.

### Logic in `transfer_money()` Method

The `transfer_money()` method in the `User` class includes various conditional checks to ensure that transfers are authorized and supported. Here's a summary of the logic:

- Transfers between different users' checking accounts are allowed.

- Transfers from own 'savings' to own 'checking' account (and vice versa) are allowed.

- Transfers between 'savings' accounts of different users are not allowed and result in an error message.

- Transfers between 'checking' and 'savings' accounts of the same user are not supported and result in an error message.

- Any other transfer attempts result in an error message.

This logic helps prevent unauthorized and unsupported transfers from occurring, ensuring that the banking system operates securely and according to the intended rules.

---
<p align="right">Completed: ２０２３年１０月０６日（金）</p>
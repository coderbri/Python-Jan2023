class BankAccount:
    
    accounts = []
    
    def __init__(self, account_name, int_rate, balance):
        self.account_name = account_name
        self.interest_rate = int_rate
        self.balance = balance
        # Upon instantiation of BankAccount, append to accounts list.
        BankAccount.accounts.append(self)
    
    def deposit(self, deposited_amount):
        self.balance += deposited_amount
        print(f"# You've deposited ${ deposited_amount }. Your balance is now: ${ self.balance }.")
        return self
    
    def withdraw(self, withdrawal_amount):
        if ( self.balance - withdrawal_amount ) >= 0:
            self.balance -= withdrawal_amount
            print(f"x You've withdrawed ${ withdrawal_amount }. Your balance is now: ${ self.balance }.")
        else:
            self.balance -= 5
            print(f"You have insufficient funds. Charging a $5 fee.\nBalance: ${ self.balance }\n")
        return self
    
    def display_account_info(self):
        print(f'{ self.account_name } Balance: ${ self.balance }')
        return self
    
    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.interest_rate)
        print(f'Balance after yield: ${ self.balance }')
        return self
    
    @classmethod
    def display_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()

print("=== Checking Account ===")
checking = BankAccount("Checking", 0.2, 1000)
checking.deposit(850).deposit(455).deposit(100).withdraw(700).yield_interest().display_account_info()

print("\n==== Savings Account ====")
savings = BankAccount("Savings", 0.075, 4500)
savings.display_account_info().deposit(90).deposit(180).withdraw(45).deposit(270).deposit(360).withdraw(225).yield_interest().display_account_info()

print("\n==== Accounts ====")
BankAccount.display_all_accounts()
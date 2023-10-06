class BankAccount:
    
    accounts = []
    def __init__( self, interest_rate, balance ):
        self.interest_rate = interest_rate
        self.balance = balance
        BankAccount.accounts.append(self)
    
    def deposit( self, amount ):
        self.balance += amount
        print(f'Depositing ${ amount }... Balance is now: ${ self.balance }.')
        return self
    
    def withdraw( self, amount ):
        if (self.balance - amount) >= 0:
            self.balance -= amount
            print(f'Withdrawing ${ amount }... Balance is now: ${ self.balance }.')
        else:
            print('You have insufficient funds. Charging a $5 fee.')
            self.balance -= 5
        return self
    
    def display_account_info( self ):
        print(f'Balance: ${ self.balance }.')
        return self
    
    def yield_interests( self ):
        if self.balance > 0:
            self.balance += (self.balance * self.interest_rate)
        print(f'Balance after yield: ${ self.balance }.')
        return self
    
    @classmethod
    def display_all_accounts( cls ):
        for account in cls.accounts:
            account.display_account_info()

import BankAccount

class User:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        # Accessing BankAccount class
        self.account = BankAccount.BankAccount( interest_rate=0.1, balance=0 )
        self.accounts = {} # account dictionary per user
    
    def display_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    # * BankAccount Management Methods
    def create_account( self, interest_rate=0.1, balance=0, account_name='checking' ):
        # ? Create first account, and only a user's first account, as 'checking' by default.
        if account_name in self.accounts:
            print('Account of this name already exists. Please Try again.')
        else:
            new_account = BankAccount.BankAccount(interest_rate, balance)
            self.accounts[account_name] = new_account
        return self
    
    # ? All deposits/withdrawals go to checking by default if not specified.
    def make_deposit( self, deposited_amount, account_name='checking' ):
        self.accounts[account_name].deposit(deposited_amount)
        # ? .deposit() method can be used as its imported from BankAccount class
        return self
    
    def make_withdrawal( self, withdrawed_amount, account_name='checking' ):
        self.accounts[account_name].withdraw(withdrawed_amount)
        return self
    
    def display_user_balance( self, account_name='checking' ):
        display_str = ''
        print(f'=== {self.first_name}\'s account summary ==='.upper())
        # retrieve key:val pairs from User's account dictionaries
        for account_name, account in self.accounts.items(): 
            display_str += f"{account_name.title()}: ${account.balance}\n"
        print(display_str)
        return self
    
    def transfer_money(self, source_account, target_account, amount_to_transfer, other_user=None):
        print("\nMoney transfer processing...\n-----------------------------")
        
        if source_account.lower() == 'checking' and target_account.lower() == 'checking' and other_user is not None:
            # Transferring between different users' checking accounts is allowed
            print(f'Transferring ${amount_to_transfer} from {self.first_name}\'s {source_account.title()} account to {other_user.first_name}\'s {target_account.title()} account.')
            self.accounts[source_account].withdraw(amount_to_transfer)
            other_user.accounts[target_account].deposit(amount_to_transfer)
            print('Transfer Complete!')
        
        elif source_account.lower() == 'savings' and target_account.lower() == 'checking' and other_user is None:
            # Transferring from own 'savings' to own 'checking' account is allowed
            print(f'[User {self.display_full_name()}] Transferring ${amount_to_transfer} from {source_account.title()} account to {target_account.title()} account.')
            self.accounts[source_account].withdraw(amount_to_transfer)
            self.accounts[target_account].deposit(amount_to_transfer)
            print('Transfer Complete!')
        
        elif source_account.lower() == 'checking' and target_account.lower() == 'savings' and other_user is None:
            # Transferring from own 'checking' to own 'savings' account is allowed
            print(f'[User {self.display_full_name()}] Transferring ${amount_to_transfer} from {source_account.title()} account to {target_account.title()} account.')
            self.accounts[source_account].withdraw(amount_to_transfer)
            self.accounts[target_account].deposit(amount_to_transfer)
            print('Transfer Complete!')
        
        elif source_account.lower() == 'savings' and target_account.lower() == 'savings':
            if other_user is not None and self.last_name != other_user.last_name:
                print('!!! Action cannot be performed. Savings cannot be transferred between users.')
        
        # elif source_account.lower() == 'checking' and target_account.lower() == 'savings' and other_user is not None:
        #     print('!!! Action cannot be performed. Unsupported or unauthorized transfer. Savings cannot be transferred between users.')
            else:
                print('!!! Action cannot be performed. Unsupported or unauthorized transfer.')
        else:
            print('!!! Action cannot be performed. Unsupported or unauthorized transfer.')
        
        return self



# * TESTING GROUND
jdoe = User("Jane", "Doe", "jdoe@mail.com")
jdoe.create_account(0.02, 200).make_deposit(50).make_withdrawal(75).display_user_balance()
jdoe.create_account(0.05, 100, 'savings').display_user_balance().make_deposit(150)

jsmithy = User("John", "Smith", "jsmith@gmail.com")
jsmithy.create_account(0, 200).display_user_balance().make_deposit(40).make_withdrawal(85)

print("\n== Transferring between checking accounts ==".upper())
jdoe.transfer_money('checking', 'checking', 50, jsmithy).transfer_money('savings', 'checking', 25)
jdoe.transfer_money('checking', 'savings', 25).display_user_balance()

print("\n== Transferring between checking & savings accounts ==".upper())
jsmithy.display_user_balance().transfer_money('checking', 'savings', 15, jdoe) # Should print error message.
jdoe.transfer_money('savings', 'savings', 15, jsmithy) # Should print error message.

print("\n== Transferring between own accounts ==".upper())
jdoe.display_user_balance()  # Should print an error message
jdoe.transfer_money('savings', 'checking', 10)  # Should print an error message
jdoe.transfer_money('checking', 'savings', 25)  # Should print an error message

# # Test invalid transfers
jsmithy.transfer_money('savings', 'savings', 10)  # Should print an error message
jsmithy.transfer_money('checking', 'checking', 10)  # Should print an error message


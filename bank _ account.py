class BalanceException(Exception):
    pass
class create_bank_account:
    def __init__(self, initial_deposit, account_name):
        self.name = account_name
        self.balance = initial_deposit

    def deposit(self, amount):
        if amount <= 0:
            raise BalanceException(
                f"\nYou can only make a deposit of $1 or more."
            )
        print("\nInitiating depsoit...🚀")
        self.balance = self.balance + amount
        print("\nDeposit completed ✅")
        self.get_balance()
    
    def get_balance(self):
        print(f"\nAccount '{self.name}' has balance ${self.balance:.2f}")

    def valid_transaction(self, amount):
        if amount > self.balance:
            raise BalanceException
        (f"\nAccount '{self.name}' on has ${self.balance:.2f}")

    def withdraw(self, amount):
       try:
            print("\nInitiating withdrawal...🚀")
            self.valid_transaction(amount)
            self.balance = self.balance - amount
            print("\nWithdrawal complete. ✅")
            self.get_balance()
       except BalanceException as error:
           print(f"\nTransaction interrupted.❌{error}")

    def transfer(self, amount, account):
        try:
            print("\nInitiating transfer...🚀")
            self.withdraw(amount)
            account.deposit(amount)
            print("\nTransfer completed.✅")
            self.get_balance()
            account.get_balance()
        except BalanceException as error:
            print(f"\n Transfer interrupted. ❌{error}")
        
class interest_rewards_account(create_bank_account):
    def deposit(self,amount):
        if amount <= 0:
            raise BalanceException(
                f"\nYou can only make a deposit of $1 or more."
            )
        print("\nInitiating depsoit...🚀")
        self.balance = self.balance + (amount * 1.2)
        print("\nDeposit completed ✅")
    
class savings_account(interest_rewards_account):
    def __init__(self,initial_deposit,account_name):
        super().__init__(initial_deposit,account_name)
        fee = 10
    
    def withdraw(self,amount):
        try:
            print("\nInitiating withdrawal...🚀")
            self.valid_transaction(amount)
            print("\nWithdrawal complete.✅")
            self.get_balance()
        except BalanceException as error:
          print(f"\nWithdrawal interrupted.❌ {error}" 
        )
        
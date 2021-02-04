class Account():

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"Account owner: {self.owner}\nAccount balance: ${self.balance}"

    def deposit(self, deposit_amount):
        self.balance += deposit_amount
        print("Deposit Accepted")
        return self.balance
    
    def withdraw(self, withdraw_amount):
        if withdraw_amount <= self.balance:
            self.balance -= withdraw_amount
            print("Withdraw Accepted")
            return True
        else:
            print("Funds Unavailable!")
            return False


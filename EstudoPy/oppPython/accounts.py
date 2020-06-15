class Account:
    """
    Simple class Account with balance.
    """
    def __init__(self, name,balance):
        self.name = name
        self.balance = balance
        print("Account created for "+ self.name)

    def deposit(self, amount):
        if amount >0:
            self.balance +=amount

    def withdraw(self, amount):
        if amount >0:
            self.balance -=amount
            
        

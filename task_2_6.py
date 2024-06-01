class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("The amount to be deposited should be greater than zero.")
        self.balance += amount

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("The amount to be withdrawn should be greater than zero.")
        if amount > self.balance:
            raise ValueError("Not enough balance.")
        self.balance -= amount

    def get_balance(self):
        return self.balance
    
account = BankAccount()

print(account.get_balance())

account.deposit(100)
print(account.get_balance())

account.withdraw(50)
print(account.get_balance())
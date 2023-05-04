class BankAccount:
    def __init__(self, owner_name, balance=0):
        self.owner_name = owner_name
        self.balance = balance
    
    def create_account(owner_name):
        return BankAccount(owner_name)
    
    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Amount must be positive")
        self.balance += amount
    
    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Amount must be positive")
        if amount > self.balance:
            raise ValueError("Not enough balance")
        self.balance -= amount
    
    def transfer(self, other_account, amount):
        self.withdraw(amount)
        other_account.deposit(amount)


account1 = BankAccount.create_account("Alice")
account2 = BankAccount.create_account("Bob")

account1.deposit(100)

account1.transfer(account2, 50)

print("---------------")
print(f"Owner: {account1.owner_name}")
print(f"Balance: {account1.balance} $")
print("---------------")
print(f"Owner: {account2.owner_name}")
print(f"Balance: {account2.balance} $")
print("---------------")
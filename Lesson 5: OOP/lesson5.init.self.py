
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def show_balance(self):
        print(f"{self.owner}'s balance: {self.balance}")

account = BankAccount("Eco", 500)
account.show_balance()
account.deposit(200)
account.show_balance()
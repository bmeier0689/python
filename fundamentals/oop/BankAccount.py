class BankAccount:
    accounts = []

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
        else:
            self.balance - 5
            print("Insufficient funds: Charging a $5 fee")
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance * self.int_rate
        return self

    @classmethod
    def all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()

acc1 = BankAccount(0.1, 100)
acc2 = BankAccount(0.2, 500)

acc1.deposit(50).deposit(50).deposit(500).withdraw(387).yield_interest().display_account_info()
acc2.deposit(500).deposit(10000).withdraw(60).withdraw(489).withdraw(200).withdraw(453).yield_interest().display_account_info()
BankAccount.all_accounts()
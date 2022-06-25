class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = {
            "checking" : BankAccount(.02, 0),
            "savings" : BankAccount(.02, 0)
        }

    def make_deposit(self, amount):
        self.account["checking"].deposit(amount)
        self.account["savings"].deposit(amount)
        return self

    def make_withdraw(self, amount):
        self.account["checking"].withdraw(amount)
        self.account["savings"].withdraw(amount)
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Checking Balance: {self.account['checking'].display_account_info()}")
        print(f"User: {self.name}, Savings Balance: {self.account['savings'].display_account_info()}")
        return self

class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if (self.balance - amount) >= 0:
            self.balance -= amount
        else:
            self.balance - 5
            print(f"Insufficient funds: Charging a $5 fee")
        return self

    def display_account_info(self):
        return f"{self.balance}"

    def yield_interest(self):
        if self.balance > 0:
            self.balance * self.int_rate
        return self

brad = User("Brad", "bmeier@gmail.com")
brad.account["checking"].deposit(1000)
brad.account["savings"].deposit(1500)
brad.display_user_balance()

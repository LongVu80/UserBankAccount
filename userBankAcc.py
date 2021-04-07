class BankAccount:
	def __init__(self, int_rate = 0, balance = 0): 
		self.rate = int_rate
		self.balance = balance

	def deposit(self, amount):
		self.balance += amount
		return self

	def withdraw(self, amount):
		if amount > self.balance:
			self.balance -= 5
			print("Insufficient Funds: Charging a $5 fee")
		elif self.balance >= amount:
			self.balance -= amount
			return self

	def display_account_info(self):
		print(f"Balance: ${self.balance}")
		return self

	def yield_interest(self):
		if self.balance > 0:
			self.balance = self.balance + self.balance * self.rate
		return self


class User:
    def __init__(self, name, email, accountNumber):
        self.username = name
        self.email = email
        self.number = accountNumber
        self.account = BankAccount(0.01)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdraw(self, amount):
        self.account.withdraw(amount)
        return self

    def user_name(self):
        print(f"User: {self.username}, Account #s: {self.number}")
        return self

    def user_account_balance(self):
        self.account.display_account_info()
        return self
        

Anthony1 = User("Anthony Smith", "AnthonyS@gmail.com", 1231)


Anthony1.make_deposit(200)
Anthony1.make_deposit(500)
Anthony1.make_deposit(300)
Anthony1.make_deposit(700)
Anthony1.make_withdraw(600)
Anthony1.user_name()
Anthony1.user_account_balance()
Anthony1.account.yield_interest().display_account_info()
Anthony1.user_account_balance()

Anthony2 = User("Anthony Smith", "AnthonyS@gmail.com", 1453)


Anthony2.make_deposit(400)
Anthony2.make_deposit(200)
Anthony2.make_deposit(500)
Anthony2.make_deposit(800)
Anthony2.make_withdraw(400)
Anthony2.user_name()
Anthony2.user_account_balance()
Anthony2.account.yield_interest().display_account_info()
Anthony2.user_account_balance()
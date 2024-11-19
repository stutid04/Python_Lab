class TransactionHistory:
    def _init_(self):
        self.transactions = []

    def add_transaction(self, transaction_type, amount, balance):
        self.transactions.append({
            "type": transaction_type,
            "amount": amount,
            "balance": balance
        })

    def show_history(self):
        print("Transaction History:")
        for transaction in self.transactions:
            print(f"{transaction['type']} - Amount: {transaction['amount']}, Balance: {transaction['balance']}")

class Account:
    def _init_(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = balance
        self.history = TransactionHistory()

    def check_balance(self):
        print(f"Balance: {self.balance}")
        return self.balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be greater than zero.")
            return
        self.balance += amount
        self.history.add_transaction("Deposit", amount, self.balance)
        print(f"Deposited: {amount}. New Balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdraw amount must be greater than zero.")
            return
        if amount > self.balance:
            print("Insufficient balance.")
            return
        self.balance -= amount
        self.history.add_transaction("Withdraw", amount, self.balance)
        print(f"Withdrew: {amount}. New Balance: {self.balance}")

class SavingAccount(Account):
    def _init_(self, account_number, name, balance=0, withdraw_limit=5000):
        super()._init_(account_number, name, balance)
        self.withdraw_limit = withdraw_limit

    def withdraw(self, amount):
        if amount > self.withdraw_limit:
            print(f"Withdraw limit exceeded. Maximum allowed: {self.withdraw_limit}")
            return
        super().withdraw(amount)

class CurrentAccount(Account):
    def _init_(self, account_number, name, balance=0, withdraw_limit=10000):
        super()._init_(account_number, name, balance)
        self.withdraw_limit = withdraw_limit

    def withdraw(self, amount):
        if amount > self.withdraw_limit:
            print(f"Withdraw limit exceeded. Maximum allowed: {self.withdraw_limit}")
            return
        super().withdraw(amount)

class CheckingAccount(Account):
    def _init_(self, account_number, name, balance=0, withdraw_limit=2000):
        super()._init_(account_number, name, balance)
        self.withdraw_limit = withdraw_limit

    def withdraw(self, amount):
        if amount > self.withdraw_limit:
            print(f"Withdraw limit exceeded. Maximum allowed: {self.withdraw_limit}")
            return
        super().withdraw(amount)

# Example Usage
saving_acc = SavingAccount("123456", "Alice", balance=10000, withdraw_limit=5000)
saving_acc.deposit(2000)
saving_acc.withdraw(3000)
saving_acc.withdraw(6000)  # Exceeds withdraw limit
saving_acc.history.show_history()

current_acc = CurrentAccount("654321", "Bob", balance=20000, withdraw_limit=10000)
current_acc.deposit(5000)
current_acc.withdraw(12000)  # Exceeds withdraw limit
current_acc.withdraw(8000)
current_acc.history.show_history()

checking_acc = CheckingAccount("987654", "Charlie", balance=5000, withdraw_limit=2000)
checking_acc.deposit(1000)
checking_acc.withdraw(2500)  # Exceeds withdraw limit
checking_acc.withdraw(1500)
checking_acc.history.show_history()
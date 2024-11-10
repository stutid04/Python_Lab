class ATM:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def check_balance(self):
        return f"Your current balance is: ${self.balance}"

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited: ${amount}. New balance: ${self.balance}"
        else:
            return "Deposit amount must be positive."

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient balance."
        elif amount <= 0:
            return "Withdrawal amount must be positive."
        else:
            self.balance -= amount
            return f"Withdrawn: ${amount}. New balance: ${self.balance}"

    def main_menu(self):
        print("Welcome to the ATM!")
        while True:
            print("\nChoose an option:")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Exit")
            choice = input("Enter option (1-4): ")
            if choice == "1":
                print(self.check_balance())
            elif choice == "2":
                amount = float(input("Enter deposit amount: "))
                print(self.deposit(amount))
            elif choice == "3":
                amount = float(input("Enter withdrawal amount: "))
                print(self.withdraw(amount))
            elif choice == "4":
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")
atm = ATM(100)
atm.main_menu()

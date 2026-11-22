class BankAccount:
    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Amount deposited successfully")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount")
        elif amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print("Amount withdrawn successfully")

    def check_balance(self):
        print(f"Account Holder : {self.name}")
        print(f"Account Number : {self.account_number}")
        print(f"Balance        : Rs {self.balance:.2f}")


name = input("Enter Account Holder Name: ")
account_number = input("Enter Account Number: ")
balance = float(input("Enter Initial Balance: "))

account = BankAccount(name, account_number, max(0, balance))

while True:
    print("\nBANK ACCOUNT MENU")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter deposit amount: "))
        account.deposit(amount)

    elif choice == "2":
        amount = float(input("Enter withdrawal amount: "))
        account.withdraw(amount)

    elif choice == "3":
        account.check_balance()

    elif choice == "4":
        print("Thank you for using Bank Account System")
        break

    else:
        print("Invalid choice")

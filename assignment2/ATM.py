class Account:
    def __init__(self, account_number, pin, balance=0):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"₹{amount} deposited successfully. Current Balance: ₹{self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Error: Insufficient balance for withdrawal.")
            return False
        self.balance -= amount
        print(f"₹{amount} withdrawn successfully. Current Balance: ₹{self.balance}")
        return True

    def check_balance(self):
        print(f"Current Balance: ₹{self.balance}")
        return self.balance


class ATMService:
    def __init__(self):
        self.accounts = {}  # Stores accounts by account number

    def create_account(self, account_number, pin, balance=0):
        if account_number in self.accounts:
            print("Error: Account number already exists.")
            return
        self.accounts[account_number] = Account(account_number, pin, balance)
        print(f"Account {account_number} created successfully!")

    def authenticate(self, account_number, pin):
        account = self.accounts.get(account_number)
        if account and account.pin == pin:
            print("Authentication successful!")
            return account
        print("Error: Invalid account number or PIN.")
        return None

    def deposit(self, account, amount):
        if amount <= 0:
            print("Error: Deposit amount must be positive.")
        else:
            account.deposit(amount)

    def withdraw(self, account, amount):
        if amount <= 0:
            print("Error: Withdrawal amount must be positive.")
        else:
            if account.withdraw(amount):
                # Simulate dispensing cash
                print("Dispensed cash as:")
                denominations = [500]
                remaining = amount
                for denom in denominations:
                    count = remaining // denom
                    if count > 0:
                        print(f"₹{denom} x {count}")
                        remaining %= denom
                if remaining > 0:
                    print(f"Remaining ₹{remaining} could not be dispensed due to unavailable denominations.")

    def check_balance(self, account):
        account.check_balance()


def admin_setup():
    atm_service = ATMService()
    # Predefine 3 user accounts
    atm_service.create_account("12345", "1111", 5000)
    atm_service.create_account("67890", "2222", 10000)
    atm_service.create_account("54321", "3333", 2000)
    return atm_service


def main():
    atm_service = admin_setup()

    while True:
        print("\n--- ATM Management System ---")
        print("1. Login")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            account_number = input("Enter Account Number: ")
            pin = input("Enter PIN: ")
            account = atm_service.authenticate(account_number, pin)
            if account:
                while True:
                    print("\n--- Account Menu ---")
                    print("1. Deposit Money")
                    print("2. Withdraw Money")
                    print("3. Check Balance")
                    print("4. Logout")
                    sub_choice = input("Enter your choice: ")

                    if sub_choice == "1":
                        amount = int(input("Enter amount to deposit: "))
                        atm_service.deposit(account, amount)
                    elif sub_choice == "2":
                        amount = int(input("Enter amount to withdraw: "))
                        atm_service.withdraw(account, amount)
                    elif sub_choice == "3":
                        atm_service.check_balance(account)
                    elif sub_choice == "4":
                        print("Logged out successfully.")
                        break
                    else:
                        print("Error: Invalid choice. Try again.")
        elif choice == "2":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Error: Invalid choice. Try again.")


if __name__ == "__main__":
    main()

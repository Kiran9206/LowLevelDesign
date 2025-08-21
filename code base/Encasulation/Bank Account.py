'''1. Bank Account Class
Task: Create a BankAccount class with:
Private attributes: account_balance and account_holder_name.
Public methods: deposit(), withdraw(), get_balance(), and set_account_holder_name().
Add proper checks for withdrawing more than the balance (should not allow it).
Ensure that the balance can only be modified through the deposit() or withdraw() methods.'''



class BankAccount:

    def __init__(self, account_holder_name=None):
        self.__account_balance = 0
        self.__account_holder_name = account_holder_name if account_holder_name else "Unknown"

    # Deposit Method
    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            print(f"Deposited {amount}. New balance: {self.__account_balance}")
        else:
            print("Deposit amount must be positive.")

    # Withdraw Method with Check
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.__account_balance:
                self.__account_balance -= amount
                print(f"Withdrew {amount}. New balance: {self.__account_balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    # Get Balance Method
    def get_balance(self):
        return self.__account_balance

    # Set Account Holder Name Method
    def set_account_holder_name(self, account_holder_name):
        if account_holder_name:
            self.__account_holder_name = account_holder_name
            print(f"Account holder name set to: {self.__account_holder_name}")
        else:
            print("Account holder name cannot be empty.")
    
    # Get Account Holder Name Method (Optional)
    def get_account_holder_name(self):
        return self.__account_holder_name


# b = BankAccount()
# b.deposit(100)
# b.withdraw(50)
# b.set_account_holder_name("Kiran")
# b.get_balance()

# --------------------------------------------------------------------------------------------------------------


    

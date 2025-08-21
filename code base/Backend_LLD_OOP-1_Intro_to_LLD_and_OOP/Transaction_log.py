
class bank_account:

    # constructor
    def __init__(self):
        self.balance = 0
        self.log_message = []


    # deposit method
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.log_message.append(f"Credit Alert: {amount} has been credited!")
        else:
            self.log_message.append(f"Credit Alert: {amount} should not be negative!")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance-= amount
                self.log_message.append(f"Debit Alert: {amount} has been debited!")
            else: self.log_message.append(f"Debit Alert: Current Balance is {self.balance}")

        else:
            self.log_message.append(f"Debit Alert: {amount} should not be negative!")

    def view_transaction(self):
        for item in self.log_message:
            print(item)


if __name__ == "__main__":
    bank_account = bank_account()
    bank_account.deposit(100)
    bank_account.deposit((0))
    bank_account.deposit(500)
    bank_account.deposit(20)
    bank_account.withdraw(-10)
    bank_account.withdraw(1000)
    bank_account.withdraw(500)
    bank_account.view_transaction()

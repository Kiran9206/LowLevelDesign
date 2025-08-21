'''
Bank Account Class Implementation in Python
Problem Statement
You are tasked with creating a Python class for managing bank accounts. The class should encapsulate the functionality required for handling account details and computing interest. Your task is to implement a Bank Account class with the following specifications:

Requirements
The Bank Account class should have three data members:
accountNumber: String (representing the account number)
balance: int (representing the current balance)
roi: double (representing the rate of interest)
The Bank Account class should have two methods:
getSimpleInterest: This method should take the time (in years) as a parameter (data type: int). It should return the Simple Interest as a double.
getBalanceWithInterest: This method should take the time (in years) as a parameter (data type: int). It should return a new balance (including simple interest) as a double.
Instructions
Implement the BankAccount class according to the specified requirements.
Ensure that the class contains the specified data members and methods.
The getSimpleInterest method should calculate and return the simple interest based on the provided time (in years) and the rate of interest (roi).
The getBalanceWithInterest method should calculate and return the new balance after adding the simple interest to the current balance based on the provided time (in years) and the rate of interest (roi).
'''

class BankAccount:

    def __init__(self, accountNumber: str, balance:int, roi:float):
        self.accountNumber = accountNumber
        self.balance = balance
        self.roi = roi

    def getSimpleInterest(self, time: int)->float:
        return self.balance * (self.roi * time) / 100

    def getBalanceWithInterest(self, time: int)->float:
        simple_interest = self.getSimpleInterest(time)
        return self.balance + simple_interest

if __name__ == "__main__":
    acount = BankAccount("123456789", 10000, 5.0)
    time = 2  # in years
    print("Simple Interest:", acount.getSimpleInterest(time))
    print("Balance with Interest:", acount.getBalanceWithInterest(time))



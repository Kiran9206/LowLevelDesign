'''
It should have 3 data members
accountNumber: String
balance: int
roi:double (Should represent rate of interest)
It should have 2 methods
getSimpleInterest: It should take time (in years) as a parameter. The data type of time should be int. It should return Simple Interest as a double.
getBalanceWithInterest: It should take time (in years) as a parameter. The data type of time should be int. It should return a new balance (including simple interest) as a double.
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

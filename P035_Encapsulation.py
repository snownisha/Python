#Encapsulation
class Account:
    def __init__(self):
        self.setBalance = 0

    def setBalance(self, balance):
        self.__balance = balance

    def getBalance(self):
        print("No Balance")


Account1 = Account()
Account1.getBalance()

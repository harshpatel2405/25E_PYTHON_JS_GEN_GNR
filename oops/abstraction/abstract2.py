from abc import ABC, abstractmethod


class Bank(ABC):
    @abstractmethod
    def calculateInterest(self, amount):
        pass

    @abstractmethod
    def deposit(self):
        pass


class SBI (Bank):
    def calculateInterest(self, amount):
        interest = amount * 0.07
        print("Interest in SBI is ", interest)


class HDFC(Bank):
    def calculateInterest(self, amount):
        interest = amount * 0.08
        print("Interest in HDFC is ", interest)


class ICICI(Bank):
    def calculateInterest(self, amount):
        interest = amount * 0.09
        print("Interest in ICICI is ", interest)

# a = Bank()
# a.calculateInterest(12000)


s = SBI()
s.calculateInterest(15000)
# s.deposit()

h = HDFC()
h.calculateInterest(50000)

i = ICICI()
i.calculateInterest(80000)

# modules and packages
# exception
# decorators (function revision)
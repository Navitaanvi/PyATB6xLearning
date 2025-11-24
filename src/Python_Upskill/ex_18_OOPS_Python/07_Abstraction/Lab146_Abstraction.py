from abc import ABC,abstractmethod

class Father(ABC):
    def __init__(self,name):
        self.name = name

    @abstractmethod
    def loan(self):
        pass

class Amit(Father):

    def loan(self):
        print("Giving the loan for the father")

amit = Amit("Amit Sharma")
amit.loan()



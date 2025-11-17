"""
You need to create a calculator function,
but the calculator function has to take the value from the parameterized constructor.
 So while creating the object, you will pass the parameters and that will
basically return the sum of the two numbers, multiplication of two numbers.
"""
class Calculator:
    a = None
    b = None

    def __init__(self,aGiven,bGiven):
        self.a = aGiven
        self.b = bGiven
    def sum(self):
        return self.a + self.b
    def sub(self):
        return self.a-self.b
    def mul(self):
        return self.a * self.b
    def div(self):
        return self.a/self.b

cal = Calculator(4,4)
print(cal.sum())
print(cal.sub())
print(cal.mul())
print(cal.div())







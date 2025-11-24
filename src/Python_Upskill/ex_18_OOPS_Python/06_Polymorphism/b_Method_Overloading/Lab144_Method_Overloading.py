class MathClass:
    def add(self,a,b):
        return a+b

    def add(self,a,b,c=10):
        return a+b+c

obj_ref = MathClass()
print(obj_ref.add(2,4))
print(obj_ref.add(1,2,30))

print("--------------------")

class Calculator:
    def sum(self,*numbers):
        total = 0
        for n in numbers:
            total+=n
        return total

obj = Calculator()
print(obj.sum(10,12))
print(obj.sum(-10,30))

print("---------")
print("Python support overloading only through default values")
print("same method behave differently with different no of arguments ")
class Calc:
    def sum(self,a=0,b=0,c=0):
        return a+b+c
c= Calc()
print(c.sum(1,2,3))
print(c.sum(2,3))
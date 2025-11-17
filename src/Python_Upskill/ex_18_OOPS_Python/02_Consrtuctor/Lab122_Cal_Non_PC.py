class Calc:
    a = None
    b = None

    def __init__(self):
        print("Default Cons")

    def sum(self,a,b):
        return a+b

    def diff(self,a,b):
        return a-b

    def mul(self,a,b):
        return a*b

    def div(self,a,b):
        return a/b

a = float(input("Enter the value of a "))
b = float(input("Enter the value of b "))

obj_ref = Calc()
summation = obj_ref.sum(a,b)
difference = obj_ref.diff(a,b)
multiplication = obj_ref.mul(a,b)
division = obj_ref.div(a,b)

print(summation,difference,multiplication,division,sep = " ** ",end = "___")


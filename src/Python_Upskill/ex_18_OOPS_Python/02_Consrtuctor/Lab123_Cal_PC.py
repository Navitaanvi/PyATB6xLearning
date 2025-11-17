class Calc:
    a = None
    b = None

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def sum(self):
        return self.a + self.b

    def diff(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a/self.b

obj_Ref = Calc(4,2)
print(obj_Ref.sum(),obj_Ref.diff(),obj_Ref.mul(),obj_Ref.div(),sep = "--",end = "###")


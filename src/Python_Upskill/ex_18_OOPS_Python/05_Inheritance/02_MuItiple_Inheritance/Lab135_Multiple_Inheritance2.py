# In multiple Inheritance, if we have different class but same method name,
# then whichever is declared first in the child class will be called.

class Father1:
    def money(self):
        print("F1 Money")

class Father2:
    def money(self):
        print("F2 Money")

# class Child(Father1,Father2):
class Child(Father2, Father1):
    def give_money(self):
        print("Son")
        self.money()

c=Child()
c.give_money()
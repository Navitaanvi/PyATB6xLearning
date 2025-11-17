a = 10   #variable everywhere in the program
class Person:
    b = 11 #instance variable

    def print_info(self):
        c = 20  #local variable
        print(c)
        print(self.b)
        print(a)

obj_ref = Person()
print(b)
print(c)

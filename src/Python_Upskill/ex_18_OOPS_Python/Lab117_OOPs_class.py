class Person:
    #Attributes
    name = None
    id = None
    age = None
    email = None
    height = None
    gender = None
    phone_no = None
    address = None

    #Behaviour
    def talk(self):
        print("I can talk")

    def sleep(self,name):
        print("I am a method")
        print("sleep!", name)

    def sleep2(self,name):
        print("I am a method!!")
        return None

    def walk(self):
        print("I am walking")

    def method_walk_return(self):
        return "I am walking"

def fun_outside():
    print("outside")

geeta = Person()
navita = Person()
#navita = object Reference
#Person() = object
# anvi = Person()
# sam = Person()
# print(geeta.name)
# print(geeta.talk)
# print(geeta.sleep("Navita"))
print(navita.talk())
print(navita.sleep("Yashu"))
print(navita.sleep2("Ruchy"))
print(navita.walk())
print(navita.method_walk_return())

print(fun_outside())

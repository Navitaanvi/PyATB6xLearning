class Utility:
    @staticmethod
    def greet_course_name(name):
        print("Hi",name)

    def greet_personal(self,name):
        print("Hello",name)

# amit = Utility()
# amit.greet("Navita")
# amit.greet_personal("Ruchy")
Utility.greet_course_name("PyATB") #static method can be called using class also.
amit = Utility()
amit.greet_personal("Ruchy")
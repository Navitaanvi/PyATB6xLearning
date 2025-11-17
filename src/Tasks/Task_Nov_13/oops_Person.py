"""
Create a Person class where we will have five attributes and five behaviors.
Make sure that each type of function is used,
and I want you to also create the print function,
which will print all the instance variable values.
"""

class Person:
    name = None
    age = None
    gender =None
    city = None
    occupation = None

    def __init__(self,nameGiven,ageGiven,genderGiven,cityGiven,occupationGiven):
        self.name = nameGiven
        self.age = ageGiven
        self.gender = genderGiven
        self.city = cityGiven
        self.occupation = occupationGiven


    def walk(self):
        print("I can walk.")
        print(self.name)

    def talk(self,name):
        print(f"{self.name } is talking to {name}")

    def sing(self):
        print("I can sing.")

    def play(self):
        print("who is playing :",self.name)

    def work(self):
        print("I can work")

    def printDetails(self):
        print("Name :", self.name)
        print("age :", self.age)
        print("Gender :", self.gender)
        print("City: ",self.city)
        print("Occupation: ",self.occupation)

person = Person("Anvi",24,"Female","Dhanbad","QA")
person.walk()
person.play()
person.talk("navita")
person.printDetails()

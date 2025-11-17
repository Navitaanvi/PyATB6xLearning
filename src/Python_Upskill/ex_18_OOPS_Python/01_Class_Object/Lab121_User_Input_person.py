class Person():
    def __init__(self):
        print("Let's take user input, Please share name,age,phone no,occupation ")
        self.name = input("Enter the name \n")
        self.age = input("Enter the age \n")
        self.phone = input("Enter the phone\n")
        self.occupation = input("Enter the occupation\n")


    def display_values(self):
        print("Name is: ",self.name ,"Age is:",self.age,"Phone is:",self.phone,"Occupation is:",self.occupation)
navita = Person()
navita.display_values()

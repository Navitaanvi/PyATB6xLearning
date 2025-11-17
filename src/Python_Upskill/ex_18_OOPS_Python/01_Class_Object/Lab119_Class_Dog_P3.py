class Dog:
    name = None
    breed = None
    height = None
    weight = None
    race = None

    def __init__(self,nameGiven,breedGiven):
        print("Parameterized constructor")
        self.name = nameGiven
        self.breed = breedGiven


    def bark(self):
        print("Bark")

    def sleep(self):
        print("Who is sleeping --->" + self.name)

    def talk(self):
        pass

chow = Dog("chipsy","pug")
rancho = Dog("rancho","Desi")

chow.sleep()
rancho.sleep()


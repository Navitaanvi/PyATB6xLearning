class Car:
    name = None
    make = None
    model = None

    def __init__(self,o_name,o_make,o_model):
        self.name = o_name
        self.make = o_make
        self.model = o_model

    def start_engine(self):
        print("Start a car with the name " + self.name)
        print("Start a car with the make " + self.make)
        print("Start a car with the model " + str(self.model))

lambo = Car("Lambo","V6",2023)
lambo.start_engine()

mg_hector = Car("Hector","1.5 + Turbo",2025)
mg_hector.start_engine()









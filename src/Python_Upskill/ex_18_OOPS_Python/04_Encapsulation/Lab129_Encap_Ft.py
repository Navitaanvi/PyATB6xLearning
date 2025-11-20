class Car:
    def __init__(self):
        self.public_navita = "navita"
        self.__private_baby = "pass123"

    def nany(self):
        self.__private_baby = "456pass"
        print(self.__private_baby)

obj_ref = Car()
print(obj_ref.public_navita)
print(obj_ref.nany())
# print(obj_ref._Car__private_baby)

# print(obj_ref.__password_secure)

##Private variable is accessible within the class.
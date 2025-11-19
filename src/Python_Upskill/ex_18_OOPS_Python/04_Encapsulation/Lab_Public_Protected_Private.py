class TestExample:
    def __init__(self):
        self.driver = "Chrome"
        self._config = "STAGING"
        self.__api__key = "abc123"

    def show(self):
        print(f"The value of driver : {self.driver}")
        print("The value of config : {} ".format(self._config))
        print(f"The value of  API Key : {self.__api__key}")

    def __private_method1(self):
        print("Private method1")

    def __private_method2(self):
        print("Private method2")

    def work(self):
        self.__private_method1()
        self.__private_method2()
obj_ref = TestExample()
obj_ref.show()
obj_ref.work()

#Access Levels
print(obj_ref.driver)  #Public :✅ Accessible everywhere
print(obj_ref._config) #Protected:⚠️ Accessible but discouraged
# print(obj_ref.__api__key) #Private:❌ AttributeError




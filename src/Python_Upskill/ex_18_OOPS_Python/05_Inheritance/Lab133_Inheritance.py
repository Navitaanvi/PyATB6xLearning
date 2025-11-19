#Single Inheritance
#A subclass/child/son inherits from one parent/Base/Father.

class BaseTest:
    driver = "chrome"
    __driver2 = "Firefox" #pri_var -- accessible within the class

    def setup(self):
        print("Base setup with the browser and env -->" + self.__driver2)


class LoginTest(BaseTest):
    def run(self):
        self.setup()
        print("Running the test cases ---> " + self.driver,"browser" )
        # print("Running the test cases ---> " + self.__driver,"browser" )


obj_ref = LoginTest()
obj_ref.run()

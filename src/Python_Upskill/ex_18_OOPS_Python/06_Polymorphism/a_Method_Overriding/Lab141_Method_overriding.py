class TestSuite:
    def info(self):
        print("Test suite information ")

class BaseTest(TestSuite):
    def setup(self):
        print("Base setup")

    def run(self):
        print("Base test execution ")

class LoginTest(BaseTest):
    def run(self):
        print("Login Test Execution")

class APITest(BaseTest):
    def run(self):
        print("API Test Execution")

# t = LoginTest()
# t = APITest()
t = BaseTest()
t.run()


class BaseTest:
    def setup(self):
        print("setup from BaseTest ")

class LoginTest(BaseTest):
    def run(self):
        print("Running Login Test ")

class SignupTest(BaseTest):
    def run(self):
        print("Running signup Test ")

LoginTest().run()
LoginTest().setup()
SignupTest().setup()
SignupTest().run()
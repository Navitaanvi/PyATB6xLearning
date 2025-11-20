class TestSuite:
    def info(self):
        print("This is Grandfather - step1 ")

class BaseTest(TestSuite):
    def setup(self):
        print("Base Test, this is Father - step2 ")

class UITest(BaseTest):
    def run(self):
        self.info()
        self.setup()
        print("Running Test cases ")

test = UITest()
test.run()


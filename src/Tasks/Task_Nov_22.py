class BaseCounter:
    count = 0

    @staticmethod
    def run_test():
        BaseCounter.count += 1
        print("Test Executed")

t1 = BaseCounter()
t1.run_test()

t2 = BaseCounter()
t2.run_test()
print("Total test executions " ,BaseCounter.count)


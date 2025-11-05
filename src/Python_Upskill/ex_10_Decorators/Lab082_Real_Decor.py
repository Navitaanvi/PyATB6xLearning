import time
def print_logs(func):
    def wrapper():
        print("start of the logs")
        func()
        print("end of logs")
    return wrapper

def time_decorator(func):
    def wrapper():
        start_time = time.time()
        print(start_time)
        func()
        end_time = time.time()
        print(end_time)
        print("Total time taken by Func --> ", end_time - start_time)
    return wrapper

@print_logs
@time_decorator
def test_ui_1():
    print("Add a func,time taken by function 1")
    time.sleep(2)

@print_logs
@time_decorator
def test_ui_2():
    print("Add a func,time taken by function 2")
    time.sleep(2)

test_ui_1()
test_ui_2()

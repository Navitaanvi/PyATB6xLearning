def before_after_UI_test(func):
    def wrapper():
        print("Before running code")
        func()
        print("After running code")
    return wrapper()

@before_after_UI_test
def test_ui():
    print("Hi, I am testing a UI Test")




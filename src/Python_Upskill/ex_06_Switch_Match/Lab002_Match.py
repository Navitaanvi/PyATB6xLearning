print("Enter which test type you want to run")
test_type = input("Enter the test type : API,UI,Performance,Security\n")

match test_type:
    case "API":
        print("We are running Postman API Test cases")
    case "UI":
        print("We are running Postman UI Test cases")
    case "Performance":
        print("We are running Postman Performance Test cases")
    case "Security":
        print("We are running Postman Security Test cases")
    case _:
        print("Invalid type")


# print("Enter which test type you want to run")
# test_type = input("Enter the test type : API, UI, Performance, Security\n")
#
# if test_type == "API":
#     print("We are running Postman API Test cases")
# elif test_type == "UI":
#     print("We are running Postman UI Test cases")
# elif test_type == "Performance":
#     print("We are running Postman Performance Test cases")
# elif test_type == "Security":
#     print("We are running Postman Security Test cases")
# else:
#     print("Invalid type")

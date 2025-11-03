"""
1️⃣ Write a Function to Check Test Case Status
Problem:
Write a function check_status(status_code) that returns:
"PASS" if status_code = 200
"FAIL" if status_code = 400 or 500
"UNKNOWN" otherwise
Example Input & Output:
print(check_status(200))   # PASS
print(check_status(500))   # FAIL
print(check_status(302))   # UNKNOWN
"""
# def check_status(status_code):
#     if status_code == 200:
#         print("PASS")
#     elif status_code == 400 or status_code == 500:
#         print("FAIL")
#     else:
#         print("UNKNOWN")
#
# check_status(200)
# check_status(400)
# check_status(501)

def check_status(status_code):
    match status_code:
        case 200:
            return "PASS"
        case 400:
            print("FAIL")
        case 500:
            print("FAIL")
        case _:
            print("UNKNOWN")

check_status(int(input("Enter the status code: ")))
print(check_status(200))




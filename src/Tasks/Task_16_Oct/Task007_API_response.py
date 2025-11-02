"""
Q - You receive an API response code from your test script.
Write an if-else block to check whether the response is successful (status code 200) or not.

I/P response = 404 , O/P ❌ Failed API Request
I/P response = 200 , O/P ✅ Passed API Request
"""

API_response  = int(input("Enter the API Response : "))

if API_response == 200 :
    print("✅ Passed API Request")

else:
    print("❌ Failed API Request")



def validate_status_code(response_code):
    if response_code == 200:
        print("Request is success")
    else:
        print("Error in the request")

validate_status_code(200)
validate_status_code(int(input("Enter the status code : ")))
validate_status_code(response_code = 201)


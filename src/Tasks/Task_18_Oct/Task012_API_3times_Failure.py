"""
An API sometimes fails due to network delays.
Write a program to retry the API call 3 times until the response code becomes 200.
If it still fails after 3 tries, print a failure message.
Hint: Use a while loop with a counter.

Expected Output Example:
Attempt 1: Response 500
Attempt 2: Response 200
✅ Test Passed
"""
count = 1
while count <=3:
    response = int(input("Enter the API response code : "))
    print(f"Attempt : {count} Response :{response}")
    if response == 200:
        print("Test Passed")
        break
    count = count +1
else:
        print("Test Failed")



# attempt = 1
# max_attempt = 3
# response = None
# while attempt <= max_attempt:
#     if response == 200:
#         print("Test Passed ")
#         break
#     else:
#         attempt= attempt+1
#
# if response != 200:
#     print("Test failed after 3 attempts")




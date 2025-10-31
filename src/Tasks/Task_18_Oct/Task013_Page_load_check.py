"""
Simulate a page loading check using a while loop.
If page_loaded becomes True within 5 seconds, print success; else timeout.

Hint: Use a counter (like wait_time) and break condition.
"""
wait_time = 1
while wait_time <=5:
    response = input("Is page loaded? (True/False)")
    if response == "True":
        print(f"The page loaded in {wait_time} seconds")
        break
    wait_time+=1

else:
    print("The page failed to load within 5 seconds")


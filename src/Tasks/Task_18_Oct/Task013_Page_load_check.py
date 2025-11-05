"""
Simulate a page loading check using a while loop.
If page_loaded becomes True within 5 seconds, print success; else timeout.

Hint: Use a counter (like wait_time) and break condition.
"""
# wait_time = 1
# while wait_time <=5:
#     response = input("Is page loaded? (True/False)")
#     if response == "True":
#         print(f"The page loaded in {wait_time} seconds")
#         break
#     wait_time+=1
# else:
#     print("The page failed to load within 5 seconds")

import time
import random
wait_time = 0
page_loaded = False

def api_response():
    return random.choice([False, False, True]
while wait_time < 5:
    page_loaded = api_response()
    if page_loaded:
        print(f" ✅ Page loaded successfully in {wait_time + 1} seconds.")
        break

    else:
        print(f" ⏳ checking... (second {wait_time + 1})")
        time.sleep(1)
        wait_time += 1

if not page_loaded:
    print(" ❌Timeout, Page failed to load in 5 sec")

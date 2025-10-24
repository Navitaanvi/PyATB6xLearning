"""
You want to check whether a web page loads within 3 seconds (performance test condition).

load_time = 4.2
⚠️ Page load too slow: 4.2 seconds
"""

page_load_time = float(input("Enter the page load time: "))

if page_load_time <= 3 :
    print(f"Page loaded successfully in {page_load_time} seconds")

else:
    print(f" ⚠️Page too slow loaded in {page_load_time} seconds")

"""
In automation, you often compare expected and actual outputs.
Write code to check if a test case passed or failed.

expected_title = "Dashboard"
actual_title = "Dashboard "

✅ Test Passed – Title matches
True - why >  Strip and convert them into the lowercase = both of them are equal.
"""

input_title ="Dashboard".strip().lower()

expected_title = "dashboard ".strip().lower()

if input_title == expected_title:
    print("✅ Test Passed – Title matches")
else:
    print("❌ Test Failed")


print("✅ Test Passed " if input_title == expected_title else "❌ Test Failed")
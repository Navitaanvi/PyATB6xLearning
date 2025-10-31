num = int(input("Enter a number: "))
if num < 0:
    print("The factorial for negative number doesn't exist")
elif num == 0 or num == 1:
    print("Factorial of the number is : 1")
else:
    factorial = 1
    for i in range(2, num + 1):
        factorial = factorial * i
    print(f"The factorial of {num} is : {factorial}")
    print("The factorial of  {} is {} ".format(num, factorial))
    print("The factorial for given no is  ", factorial)


import math
num = int(input("Enter a no : "))
if num < 0:
    print("Doesn't exist")
else:
    print(math.factorial(num))

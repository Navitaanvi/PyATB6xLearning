#Take 2 input from the user
#Print Quotient and Remainder
# Floor division is also called quotient

num1 = int(input("Enter the first number"))
num2 = int(input("Enter the second number"))

quotient = num1//num2
remainder = num1%num2

print("The quotient is :",quotient)
print("The remainder is :",remainder)

print(f" the quotient is : {quotient} , remainder is :{remainder}")

print("The quotient : {},  the remainder :{}".format(quotient,remainder))
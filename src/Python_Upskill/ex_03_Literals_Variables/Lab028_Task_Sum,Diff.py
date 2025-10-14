#Take 3 input from the user
#Perform add, sub, mul, div

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

sum = num1+num2+num3
diff = num1-num2-num3
mul = num1*num2*num3
div = (num1/num2)/num3

print(sum)
print(diff)
print(mul)
print(div)

print(f"Addition: {sum} ,Sub :{diff} ,Mul :{mul} ,Div :{div}")

print("Addition: {}, Subtraction :{}, Multilpcation:{}, Division:{} ".format(sum,diff,mul,div))
#User Define
#1 Non return
#return something
#Parametres
#No parameters / arguments

import math
result = max(3,4)
print(result)

#1 Non return
def greet():
    print("Hello")
greet()

#2 No return type with Arguments
def greet_by_name(name):
    print("Hello",name)
greet_by_name("Navita")

#3 No return type and with default parameters
def say_hello_defalut_arg(name = "navita"):
    print("Hello",name.upper())
say_hello_defalut_arg()
say_hello_defalut_arg("Ruchy")

def multiple_arg(name1="A",name2="B"):
    print("Mul-->",name1,name2)
multiple_arg()
multiple_arg(name1="Navita",name2="Kumari")
multiple_arg(name1="ruchy")
multiple_arg(name2="Kumari")

#4 Argument + return type

def sum_of_two(a,b):
    return a+b
result = sum_of_two(4,5)
print(result)

def sum_of_two_with_default(num1= 100,num2=100):
    print("I will sum two numbers")
    return num1+num2

print(sum_of_two_with_default(200,300))
print(sum_of_two_with_default())
print(sum_of_two_with_default(num1=400))
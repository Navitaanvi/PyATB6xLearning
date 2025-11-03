num1=int(input("Enter the 1st no :"))
num2=int(input("Enter the 2nd no :"))
num3=int(input("Enter the 3rd no :"))

def sum_of_three(n1=100,n2=200,n3=300):
    return n1+n2+n3

sum_of_three(num1,num2,num3)
print(sum_of_three(num1,num2,num3))
result1=sum_of_three(n1=1000,n2=1000,n3=1000)
print(result1)
print(sum_of_three(n1=500))
print(sum_of_three(1,2,3,))
print(sum_of_three(1,2,n3=num3))



user_input = int(input("enter the number:"))

check_even_odd_f = lambda num:"even" if num%2==0 else "Odd"
result = check_even_odd_f(user_input)
print(result)

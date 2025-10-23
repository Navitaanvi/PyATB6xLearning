#WAP to take user age and
#Let him know if he can go to the club
#21

#Logic Building Formula
#step1
#i/p - age, int
#o/p -

#step 2 Rough logic

"""
age > 21 - print  can go
age< 21 - print can/t go

Step 3: write Logic

Step 4: Edge cases

Negative ages or extremely high values -- program will break
Non-numeric input - ABC
Age which is valid > 130
optimise the code

Step 5 :
Optimise the code
Handle all edge cases
"""

age = int(input("Enter the age: \n" ).strip())

if age<=0 or age > 130:
    print("enter a valid age")

else:
    if age >= 21:
        print("Can go to club")
    else:
        print("Can't go to club")



"""
*
**
***
Seperator works if multiple print arguments. end print after each print execution
"""


for i in range(3):
    for j in range(3):
        if i >= j:
            print("*",end = " ")
    print()

print("_____________________")

# rows=4
# for i in range(1,rows+1):
#     print("*" * i,end = " ")

# rows = 4
# for i in range(1, rows+1):
#     print(" ".join(['*'] * i))

row=10
for i in range(1,row+1):
    print(" ".join(["*"] * i))





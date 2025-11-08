"""
*
**
***
****
*****
"""
rows = 5
for i in range(1,rows+1):
    print("*" * i)


"""
    *
   **
  ***
 ****
*****   
"""
rows = 5
for i in range(1,rows+1):
    print(" "*(rows-1) + "*" * i)

print("_________________________")

for i in range(3):
    for j in range(3):
        if i >= j:
            print("*", end="")
    print()

#Frequency of a character in a string:
string = input("enter the string :")
char_count = {}
for char in string:
    char_count[char] = char_count.get(char,0) + 1
print(char_count)

print("--------------------------")

name = "Navitaa"
count = 0
for i in name:
    count+=1
print("Total characters:",count)














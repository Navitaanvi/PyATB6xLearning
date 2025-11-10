#Find the first non-repeating character in a string using sets
#swiss --> w
# print("swiss".count("s"))
# print("swiss".count("w"))
# print("swiss".count("i"))

def first_non_repeating(string):
    for char in string:
        if string.count(char) == 1:
            return char
        # else:   # not needed as it stops after first letter
        #     return None
    return None
print(first_non_repeating("swiss"))
print(first_non_repeating("annusinha"))

#Print all non-repeating character

s = set()
def non_repeating_characters(string):
    for char in string:
        if string.count(char) == 1:
            s.add(char)

    return s

print(non_repeating_characters("swweeinsszy"))
print(s)


















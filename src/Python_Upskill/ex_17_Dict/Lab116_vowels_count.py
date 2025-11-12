input_string = "Hello World!"

vowels = "aeiou"
vowels_count =  0
result = list()
unique_vowels = set()

for char in input_string:
    if char in vowels:
        vowels_count+=1
        result.append(char)
        unique_vowels.add(char)

print(vowels_count)
print(result)
print(unique_vowels)

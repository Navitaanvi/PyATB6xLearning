string = input("Enter a string:")
vowels = "aeiou"
vowel_count = 0
consonant_count = 0

for char in string:
    if char in vowels:
        vowel_count+=1
    else:
        consonant_count+=1
print(vowel_count)
print(consonant_count)

string = input("Enter a string:")
def palindrome(string):
    return string[::-1]

if string == string[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")


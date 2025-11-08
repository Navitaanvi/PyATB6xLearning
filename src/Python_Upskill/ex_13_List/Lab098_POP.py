#List Creation and Comprehension
# Shortcut to create a list
squares = [1, 4, 9, 16, 25]
print(squares)
print(squares.pop()) #Remove and return item at index (default last).
print(squares)
print(squares.pop(1))
print(squares)

squares.clear()
print(squares)

#index(element,start,end)
#Returns the index of the first occurrence of the element.
numbers = [1,2,3,5,66,77,99,3,77]
print("Index of 77 is ",numbers.index(77))
print("Count of 77 :",numbers.count(77))
print("sorted numbers :",numbers.sort())
print(numbers)
print("Reversed numbers :", numbers.sort(reverse=True))
print(numbers)

# max() / min() / sum() Works for numerical lists.
print("max_no =",max(numbers))
print("min_no =",min(numbers))
print("Sum =",sum(numbers))

# Slicing
print(numbers) #[99, 77, 77, 66, 5, 3, 3, 2, 1]
print(numbers[1:4])
print(numbers[-1])

print("apple" in numbers)
print(1 in numbers)

# List Creation and Comprehension
# range(1,5)---> list
l = list(range(1,5))
print(l)

# new_list = [expression for item in iterable if condition]
# expression → what you want to put in the list
#
# iterable → sequence (like list, range, string, etc.)
#
# condition → optional filter
#List Comprehension
squares = [x**2 for x in range(1,6)]
print(squares)

square = lambda x:x**2
print(square(5))

#Nested List
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix[1][1])

# del statement - Deletes an element by index or the whole list.
del numbers[0]
print(numbers)
del numbers[1:3]
print(numbers)
del(numbers[:])
print(numbers)

del numbers
print(numbers) #NameError: name 'numbers' is not defined.

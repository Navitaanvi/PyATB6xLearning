my_list = [1,2,3]
my_list[0] = "Navita"
print(my_list)

for item in my_list:
    print(item)
#range() is a function which returns list
for i in range(1,5):
    print(i)

my_list= [1,2,3]
print("element at index 0 ",my_list[0])
print("element at index 1 ",my_list[1])
print("element at index 2 ",my_list[2])

#append() - #Append at the end of the list

my_list.append(4)
print(my_list)
my_list.append(5)
print(my_list)
#extend - Append a new list

my_list.extend([6,7,8,9,10])

#insert() --> insert at a particular index
my_list.insert(1,"Anvi")
print(my_list)
print(len(my_list))

my_list.insert(0,0)
print(my_list)

my_list[1] = "Kumari"
print(my_list)

my_list.remove("Kumari")
print(my_list)

my_copy_list = my_list.copy()
print(my_list)
print(my_copy_list)

#list.remove(x) removes only the first occurrence of the given value x from the list.
my_copy_list.remove("Anvi")
print(my_list)
print(my_copy_list)



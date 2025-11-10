a={1,2,3}
b={3,4,5}
print(a|b)
print(a.union(b))


print(a&b)
print(a.intersection(b))

print(a-b) #present in a but not in b
print(b-a)

print(a^b) # remove the common
print(b^a)

set1 = {1,2,3}
set2 ={4,5,6}
set = set1.union(set2)
print(set)

set1={1,2,3,4,5}
set2={4,5,6,7,8}

my_set = set1.intersection(set2)
print(my_set)

my_set = set1.difference(set2) #present in set1 but not in set2
print(my_set)

my_set = set2.difference(set1)
print(my_set)

#Symmetric difference (returns all elements that are in either set1 or set2,👉 but not in both.)

my_set = set1^set2 # remove the common
print(my_set)



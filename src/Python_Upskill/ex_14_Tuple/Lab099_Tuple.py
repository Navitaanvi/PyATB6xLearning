#ordered and immutable collection of data

my_tuple = (1,2,3)
print(my_tuple)
#my_tuple[0] = 12 #TypeError: 'tuple' object does not support item assignment

info = ("Pramod",34,True,9.8)
print(info)

single = (3,)
print(type(single)) #<class 'tuple'>

single1 =(4)
print(type(single1)) #<class 'int'>
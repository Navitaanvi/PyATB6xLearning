shopping_list = ["bread", "butter", "Paneer"]
shopping_list[2] = "Milk"
print(shopping_list)

#Real Example
my_tuple = ("tta.com","sdet.live")
print(my_tuple)
#my_tuple.append("qa.com")
#print(my_tuple) #AttributeError: 'tuple' object has no attribute 'append'

my_api_list = list(my_tuple)
my_api_list.append("item2")
print("updated_list ",my_tuple)

my_api_list2 = tuple(my_api_list)
print("updated_tuple ",my_api_list2)

hero1 = ("Batman","Bruce wayne")

# Real case, where we Tuples
API_URLSs = ("https://sdet.live/python0x", "https://awesomeqa.com", "https://thetestingacademy.com")
print(API_URLSs[0])
print(API_URLSs[1])

t= tuple()
print(t)

l = list()
print(l)

# Conversion List to Tuple
t1 = tuple(["pramod", "amit", "manisha"])
print(t1)

hero1 = ("Batman", "Bruce Wayne")
hero2 = ("Wonder Woman", "Diana Prince")
new_tuple = (hero1,hero2)
print(new_tuple)
print(new_tuple[0][0])
print(new_tuple[1][1])

nums  =[1,2,3,4,5,6]
def even_num(x):
    return x % 2 == 0
even_numbers= list(filter(even_num,nums))
print(even_numbers)

list_student = [50,55,89,65]

def keep(x):
    if x > 50:
        return True
all_student = list(filter(keep,list_student))
print(all_student)
student_info1 = {
    "name" : "Navita",
    "age" :34,
    "address": {
        "home_add":"IND",
        "office_add":"KA"
    }
}
student_info2 = {
    "name" : "Kumari",
    "age" :10,
    "address": {
        "home_add":"ND",
        "office_add":"MAHA"
    }
}

student_list = [student_info1,student_info2]
print(student_list)

print(student_list[0])
print(student_list[1])
print(student_list[0]["name"])
print(student_list[0]["address"]["office_add"])







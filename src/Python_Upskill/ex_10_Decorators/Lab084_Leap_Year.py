def check_leap_year(year):
    if (year % 4 == 0 and year % 100 !=0) or (year % 400 == 0):
        return True
    else:
        return False

year = 5000
result = check_leap_year(year)
print(result)

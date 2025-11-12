#func that returns max value from a dictionary
#{"a":10,"b":20,"c":30}

def max_value_dict(dictionary):
    return max(dictionary.values())
print(max_value_dict({"a":10,"b":20,"c":30}))

def min_value_dict(dictionary):
    return min(dictionary.values())
print(min_value_dict({"a":10,"b":20,"c":30}))

def max_key_dict(dictionary):
    return max(dictionary.keys())
print(max_key_dict({"a":10,"b":20,"c":30}))


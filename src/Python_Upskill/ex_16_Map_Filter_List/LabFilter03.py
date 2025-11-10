names = ["QA", "", "Automation", "", "Tester"]

# non_empty = list(filter(None,names))
def non_empty(x):
    if x!="":   #Non-empty
        return True
    return None
non_empty = list(filter(non_empty,names)) #removes empty strings
print(non_empty)

#Filter returns the element which returns True

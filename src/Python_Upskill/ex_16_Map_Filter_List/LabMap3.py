response_time_ms = [1200,1500,1800]

def time_in_milisec(x):
    return x/1000

print(time_in_milisec(10000))

seconds = list(map(time_in_milisec,response_time_ms))
seconds1 = list(map(lambda x : x/1000,response_time_ms))

print(seconds)
print(seconds1)

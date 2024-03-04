string= input()
def func(string):
    upper_count = 0
    lower_count = 0
    for i in string:
        if i.isupper():
            upper_count+=1
        elif i.islower():
            lower_count+=1
    return upper_count, lower_count

print(func(string))



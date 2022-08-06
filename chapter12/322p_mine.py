import string

s = input()

list = []
num = 0

for i in s:
    if i in string.ascii_letters:
        list.append(i)
    elif i in string.digits:
        num += int(i)

list.sort()
    
result = ''.join(list) + str(num) 

print(result)
import string

a = input()

number = 0

b = []

for i in a:
    if i in string.digits:    
        number += int(i)
    if i in string.ascii_uppercase:
        b.append(i)

b.sort()

b.append(str(number))

print(''.join(b))
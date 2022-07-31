n = int(input())

move = input().split()

x = 1
y = 1

for i in move:
    print(i)
    if i == "R" and y < n:
        y += 1
    if i == "L" and y >= 1:
        y -= 1
    if i == "U" and x > 1:
        x -= 1
    if i == "D" and x < n:
        x += 1

    print(x, y)
    
print(x, y)
    
n, m = map(int, input().split())

data = list(map(int, input().split()))

data.sort()

result = 0

for x in range(n):
    for y in range(n):
        if data[x] < data[y]:
            result += 1
        
print(result)
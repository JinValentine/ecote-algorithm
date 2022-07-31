t = int(input())

count = 0

for i in range(t+1):
    for m in range(60):
        for s in range(60):
            time = str(i) + str(m) + str(s)
            if "3" in time:
                count += 1
                
print(count)
print("end")
n = list(map(int, input()))

length = len(n)

divide = length // 2

left_sum = 0
right_sum = 0

for i in range(divide):
    left_sum += n[i]
    
for i in range(divide, length):
    right_sum += n[i]
    
    
if left_sum == right_sum:
    print('LUCKY')
else:
    print('READY')
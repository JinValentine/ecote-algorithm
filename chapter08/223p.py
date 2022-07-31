n = int(input())

d = [0] * 1001

d[1] = 1
d[2] = 3

for i in range(3, n + 1):
   d[i] = (d[i - 1] + 2 * d[i - 2] ) % 796796
    #d[i - 1] 때 1가지의 경우와 d[i - 2] 때 2가지의 경우를 더한 경우의 수


print(d[n]) 
n, m = map(int, input().split())

array = []

for i in range(n):
    array.append(int(input()))

#최대 크기가 10000이므로 불가능한 수로 설정
d = [10001] * (m + 1)

#다이나믹 프로그래밍(보텀업)
#각 화폐단위마다 모든 금액을 확인해주면서 최소한의 화폐개수를 갱신해준다.
d[0] = 0
for i in range(n):
    for j in range(array[i], m + 1):
        if d[j - array[i]] != 10001: #현재 화폐를 뺀 값에서 최소한의 화폐 개수 값이 존재하는 지 확인
            d[j] = min(d[j], d[j - array[i] + 1])
            # 다른 화폐단위일 때 갱신된 값과 현재 화폐단위일 떄의 값 중 최소 값 중 비교
            

if d[m] == 10001:
    print(-1)
else:
    print(d[m])
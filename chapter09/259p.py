#모든 경로는 양방향, 1의 거리를 가지고 있다.
INF = int(1e9)
#n은 전체 회사의 개수 m은 경로의 개수
n, m = map(int, input().split())

graph = [[INF] * (n + 1) for i in range(n + 1)]

for i in range(n + 1):
    for j in range(n + 1):
        if i == j:
            graph[i][j] = 0

#연결된 두 회사의 번호가 공백으로 입력
for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1 # 양방향으로 연결되어 있고 1의 거리이기 때문에
 
#k는 중간에 들려야하는 곳 x는 최종 목적지    
x, k = map(int, input().split())

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
            
# 수행된 결과 출력
distance = graph[1][k] + graph[k][x]

# 도달할 수 없는 경우 -1을 출력
if distance >= INF: # 최소 INF + 1이면 안됨
    print("-1")
else:
    print(distance)


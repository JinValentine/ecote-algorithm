import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

# n 도시의 개수, m 통로의 개수, c 메시지를 보내고자 하는 도시
n, m, c = map(int, input().split())

graph = [[] for _ in range(n + 1)]

distance = [INF] * (n + 1)

# x는 출발도시 y는 도착도시 z 메세지 전달에 걸리는 시간
for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)         
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]: 
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(c)

# 도달 할 수 있는 노드의 개수
count = 0

# 도달 할 수 있는 노드 중에서, 가장 멀리 있는 노드와의 최단거리
max_distance = 0

for d in distance:
    #도달할 수 있는 노드인 경우
    if d != INF:
        count += 1
        max_distance = max(max_distance, d)

# 시작 노드는 제외해야 하므로 count - 1을 출력
print(count - 1, max_distance)
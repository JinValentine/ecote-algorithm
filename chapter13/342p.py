n , m = map(int, input().split())
data = [] # 초기 맵 리스트

# 3개의 벽을 설치하는 모든 경우의 수를 계산하기 때문에 
# 초기의 맵에 값을 계속 넣고 뺋 수 없기 때문에 임의로 만들어준다.
temp = [[0] * m for _ in range(n)] # 벽을 설치한 뒤의 맵 리스트

for _ in range(n):
    data.append(list(map(int, input().split())))

# 4가지의 이동 방향에 대한 리스트
# 위, 오른, 왼, 아래
# 북,  동,  남,  서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0

# 깊이 우선 탐색(DFS)을 이용해 각 바이러스가 사방으로 퍼지도록 하기
def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 상, 하, 좌, 우 중에서 바이러스가 퍼질 수 있는 경우
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if temp[nx][ny] == 0:
                # 해당 위치에 바이러스 배치하고, 다시 재귀적으로 수행
                temp[nx][ny] = 2
                virus(nx, ny)

# 현재 맵에서 안전 영역의 크기를 계산하는 메서드
def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score

# 깊이 우선 탐색(DFS)을 이용해 울타리를 설치하면서, 매번 안전 영역의 크기 계산
def dfs(count):
    global result
    # 울타리가 3개 설치된 경우
    if count == 3:
        for i in range(n):
            for j in range(m):
                # 임시 맵리스트에 초기 맵리스트를 넣어준다.
                temp[i][j] = data[i][j]
        # 각 바이러스의 위치에서 전파 진행
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    # 자리에 바이러스가 있기때문에 전파
                    virus(i, j)
        # 안전 영역의 최댓값 계산 
        # 계속적으로 지금까지 result값과 현재의 값 중 최댓값을 찾아낸다.
        result = max(result, get_score())
        # count 3개 이후로는 탐색하지 않기 때문에 재귀함수를 끝내기 위해 return한다.
        return
    
    # 빈 공간에 울타리 설치
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                # 울타리 설치
                data[i][j] = 1
                count += 1
                # 울타리 설치 했으니까 재귀함수로 보내 게속 확인
                dfs(count)
                # return 온 것은 계산된 경우로 이제 필요 없기 때문에
                # 해당 구역은 0으로 만들어주고 count를 -1 빼주고 계속해서 완전탐색한다.
                data[i][j] = 0
                count -= 1

dfs(0)
print(result)
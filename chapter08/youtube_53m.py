#어렵다 ..


for tc in range(int((input))):
    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    
    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index:index + m]) #2차원 데이터로 만들기 위해서
        index += m
    
    #다이나믹 프로그래밍 (BottomUp) 열 기준으로 데이터를 확인하며 테이블을 갱신한다.
    for j in range(1, m):
        for i in range(n):
            
            #왼쪽 위에서 오는 경우
            if i == 0 : left_up = 0 # i의 좌표가 o일 때는 left_up이 존재하지 않기 때문에 0이 나온다.
            else: left_up = dp[i - 1][j - 1]
            
            #왼쪽 아래에서 오는 경우
            if i == n - 1: left_down = 0
            else: left_down = dp[i + 1][j - 1]
            
            #왼쪽에서 오는 경우
            left = dp[i][j - 1]
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)
    
    result = 0
    
    for i in range(n):
        result = max(result, dp[i][m - 1])
    print(result)
# n * n 도시
# 빈칸, 치킨집 ,집
# 도시 (r, c) r행 c열 r과 c는 1부터 시작
# 치킨거리: 집과 가장 가까운 치킨 거리
#  도시의 치킨 거리: 모든 집의 치킨 거리의 합
# 0은 빈칸 1은 집 2는 치킨집
# 치킨집의 개수는 최대 M개를 고르고 나머지 치킨집은 모두 폐업
# 도시의 치킨 거리가 가장 작게 될지 구하는 프로그램 작성

from itertools import combinations

n, m = map(int, input().split())
chicken, house = [], []

for r in range(n):
    data = list(map(int, input().split()))
    for c in range(n):
        if data[c] == 1:
            house.append((r, c)) # 일반 집
        elif data[c] == 2:
            chicken.append((r, c)) # 치킨 집

# 모든 치킨집 중에서 m개의 치킨집을 뽑는 조합 계산
candidates = list(combinations(chicken, m))

# 치킨 거리의 합을 계산하는 함수
def get_sum(candidate):
    result = 0
    # 모든 집에 대하여
    for hx, hy in house:
        # 가장 가까운 치킨집을 찾기
        temp = 1e9
        for cx, cy in candidate:
            temp = min(temp, abs(hx - cx) + abs(hy - cy))
        # 가장 가까운 치킨집까지의 거리를 더하기
        result += temp
    # 치킨 거리의 합 반환
    return result

# 치킨 거리의 합의 최소를 찾아 출력
result = 1e9
for candidate in candidates:
    result = min(result, get_sum(candidate))
    
print(result)
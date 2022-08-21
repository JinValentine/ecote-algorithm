# 힙은 특정한 규칙을 가지는 트리
# 최댓값과 최솟값을 찾는 연산을 빠르게 하기 위해 고안된 완전이진트리

import sys
import heapq
input = sys.stdin.readline

# 파이썬에서는 기본적으로 최소 힙 구조로 작동한다.
def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))
    
res = heapsort(arr)

for i in range(n):
    print(res[i])
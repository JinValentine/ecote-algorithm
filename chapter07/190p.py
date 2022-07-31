def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    #  "//" : 나눗셈의 몫 - 나눗셈 결과의 '몫'을 가져옴

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    elif array[mid] < target:
        return binary_search(array, target, mid + 1, end)

n, target = list(map(int, input().split()))

array = list(map(int, input().split()))

result = binary_search(array, target, 0, n - 1)

if result == None:
    print("원소가 존재하지 않습니다.")

else:
    print(result + 1)
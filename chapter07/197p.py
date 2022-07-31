n = int(input())

part = list(map(int, input().split()))

m = int(input())

part_want = list(map(int, input().split()))

part.sort()

print(part)

def binary_search(array, target, start, end):
    while start <= end:
        mid = ( start + end ) // 2
    
        if array[mid] == target:
            return "yes"
        
        elif array[mid] > target:
            end = mid - 1
        
        else : 
            start = mid + 1
    
    return "no"    
    
    
    
    
for i in range(m):
    print(binary_search(part, part_want[i], 0, n-1), end=" ")
    
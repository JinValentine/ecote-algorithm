n = int(input())

array = []

for i in range(n):
    input_data = input().split()
    array.append((input_data[0], input_data[1]))
    
score = sorted(array, key=lambda student: student[1]) #lambda 매개변수 : 표현식

for student in score:
    print(student[0], end=' ')
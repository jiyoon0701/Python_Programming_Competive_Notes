data, data2 = map(int, input().split())

A =[]
B =[]

for i in range(data):
    A.append(list(map(int, input().split())))
for i in range(data):
    B.append(list(map(int, input().split())))
    
for i in range(data):
    for j in range(data2):
        print(A[i][j] + B[i][j], end = " ")
    print()

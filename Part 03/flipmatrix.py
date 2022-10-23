'''
완전 탐색 기법

입력
1

출력
1 1 1 1 1 1 1 1 1 1 
1 0 0 0 0 0 0 0 0 0 
1 0 0 0 0 0 0 0 0 0 
1 0 0 0 0 0 0 0 0 0 
1 0 0 0 0 0 0 0 0 0 
1 0 0 0 0 0 0 0 0 0 
1 0 0 0 0 0 0 0 0 0 
1 0 0 0 0 0 0 0 0 0 
1 0 0 0 0 0 0 0 0 0 
1 0 0 0 0 0 0 0 0 0 

입력2
3

출력2
1 0 0 1 1 1 1 1 1 1
0 1 0 1 1 1 1 1 1 1
0 0 1 1 1 1 1 1 1 1
1 1 1 0 0 0 0 0 0 0
1 1 1 0 0 0 0 0 0 0
1 1 1 0 0 0 0 0 0 0
1 1 1 0 0 0 0 0 0 0
1 1 1 0 0 0 0 0 0 0
1 1 1 0 0 0 0 0 0 0
1 1 1 0 0 0 0 0 0 0

'''

n = int(input())
arr = [[0]*10 for _ in range(10)]
for i in range(n): # 0
    for j in range(10): # 행
        if arr[i][j] == 0:
           arr[i][j] = 1
        else :
            arr[i][j] = 0 
            
    for k in range(10):
        if i==k:
            continue
        elif arr[k][i] == 0:
            arr[k][i] = 1
        else :
            arr[k][i] = 0
            
for i in arr:
    for j in i:
        print(j, end = ' ')
    print()
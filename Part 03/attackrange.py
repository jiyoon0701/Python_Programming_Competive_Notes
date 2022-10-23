'''
완전 탐색 기법

입력
8
4 5 3

출력
0 0 0 0 3 0 0 0
0 0 0 3 2 3 0 0
0 0 3 2 1 2 3 0
0 3 2 1 x 1 2 3
0 0 3 2 1 2 3 0
0 0 0 3 2 3 0 0
0 0 0 0 3 0 0 0
0 0 0 0 0 0 0 0

입력2
6
2 3 3

출력2
3 2 1 2 3 0
2 1 x 1 2 3
3 2 1 2 3 0
0 3 2 3 0 0
0 0 3 0 0 0
0 0 0 0 0 0

'''
n = int(input())
X, Y, R = list(map(int, input().split()))
arr = [[0]*n for _ in range(n)]

# 거리를 구해야함 (i,j) ~ (x,y)
for i in range(n):
    for j in range(n):
        dic_col = abs(i+1-X)
        dic_row = abs(j+1-Y)
        
        dic =  dic_col + dic_row
        if dic == 0: # 자기 위치
            print('x', end = ' ')
        elif dic <= R:
            print(dic, end = ' ')
        else :
            print(0, end = ' ')
    print()
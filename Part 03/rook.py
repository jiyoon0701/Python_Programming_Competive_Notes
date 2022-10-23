'''
완전 탐색 기법

입력
0 3 0 0 0 0 0 0
3 1 0 0 0 0 2 0
0 3 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0

출력
1

입력2
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 3 3 0 0 0 0 0
3 0 1 0 3 0 2 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0

출력2
0

'''
# 1 킹 2 록  3기물 
n = 8
chess = [list(map(int, input().split())) for _ in range(n)]
flag = False
for i in range(n): # 완전 탐색으로 rook을 찾아야 함.
    for j in range(n):
        if chess[i][j] == 2: # rook의 위치
            # 찾은 rook의 위치에서 행 열을 통해 킹을 죽일 수 있는지 확인해야함
            # 행 : rook의 위치를 기준으로 왼쪽, 오른쪽 확인
            for k in range(j-1, -1, -1): # 행 왼쪽 
                if chess[i][k] == 1 :
                    flag = True
                elif chess[i][k] == 3 :
                    break
            for h in range(j+1,n):
                if chess[i][k] == 1 :
                    flag = True
                elif chess[i][k] == 3 :
                    break
            # 열
            for k in range(i-1,-1,-1):   # 열 top 
                if chess[k][j] == 1:
                    flag = True
                elif chess[k][j] == 3:
                    break
                
            for h in range(i+1,n): # 열 botton
                if chess[h][j] == 1:
                    flag = True
                elif chess[h][j] == 3:
                    break
if flag :                    
    print("1")
else :
    print("0")                
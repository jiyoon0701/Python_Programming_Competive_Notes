'''
깊이 우선 탐색

입력
7 6
12

출력
7 6

'''

c, r = map(int, input().split())
arr = [[0] * (c+1) for _ in range(r+1)]
 
k = int(input())
 
if k > c * r: # 이동횟수가 더 많은 경우
    print(0)
    exit()
 
# 칸막이 생성
for i in range(r + 1):
    arr[i][c] = -1
for i in range(c + 1):
    arr[r][i] = -1
 
i, j = 0, 0
cnt = 0 #방향 조절 총 방향은 위 아래 왼쪽 오른쪽
n = 1 # 이동 횟수
arr[0][0] = 1
 
while n != k:
    if cnt % 4 == 0: # ↑ 
        if arr[i + 1][j] == 0:
            n += 1
            i += 1
            arr[i][j] = n
        else:
            cnt += 1
 
    elif cnt % 4 == 1: # →
        if arr[i][j + 1] == 0:
            arr[i][j] = n
            n += 1
            j += 1
        else:
            cnt += 1
 
    elif cnt % 4 == 2: # ↓
        if arr[i - 1][j] == 0:
            n += 1
            i -= 1
            arr[i][j] = n
        else:
            cnt += 1
 
    else: #cnt == 3: ←
        if arr[i][j - 1] == 0:
            n += 1
            j -= 1
            arr[i][j] = n
        else:
            cnt += 1
 
print(j + 1, i + 1)

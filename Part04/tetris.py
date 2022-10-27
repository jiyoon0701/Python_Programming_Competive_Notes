# '''
# 완전 탐색 기법

# 입력
# 6 7
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 1 1 1 0 0 1
# 1 1 1 0 0 1
# 1 1 1 0 1 1
# 1 1 1 0 1 1
# 1 1 1 0 1 1

# 출력
# 4 3

# '''
c, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(r)]

possible = []
possible_copy = []
score = 0
score_case = []
max_score = 0
 
for j in range(c):
    cnt = 0
    for i in range(r):
        if arr[i][j] == 1: # 1이 닿기 전까지 넣을 수 있다.
            possible.append([i-1, j])
            possible_copy.append([i-1, j])
            cnt += 1
            break
        if i == r-1 and cnt == 0: # 마지막 행에 도착했는데 1을 한 번도 못 만났다
            # 이것 또한 막대를 놓을 수 있다.
            possible.append([r-1, j])
            possible_copy.append([r-1, j])
 
for i in range(len(possible)):
    if possible[i][0] - 3 < 0: # 4칸을 넣어야 함.
        possible_copy.remove(possible[i]) # 조건에 해당 안됨 -> 채울 수가 없음 
 
for i in range(len(possible_copy)):
    y, x = possible_copy[i]
    score = 0
    for j in range(y, y-4, -1):
        arr[j][x] = 1
 
    for k in range(len(arr)):
        if 0 not in arr[k]:
            score += 1
 
    for l in range(y, y-4, -1):
        arr[l][x] = 0
 
    score_case.append([score, y, x])
 
 
for i in range(len(score_case)):
    if score_case[i][0] > max_score:
        max_score = score_case[i][0]
 
if len(score_case) == 0 or max_score == 0:
    print(0, 0)
else:
    for i in range(len(score_case)):
        if score_case[i][0] == max_score:
            print(score_case[i][2]+1, score_case[i][0])
            break
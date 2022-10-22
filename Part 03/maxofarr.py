'''
완전 탐색 기법

예제 입력
3 23 85 34 17 74 25 52 65
10 7 39 42 88 52 14 72 63
87 42 18 78 53 45 18 84 53
34 28 64 85 12 16 75 36 55
21 77 45 35 28 75 90 76 1
25 87 65 15 28 11 37 28 74
65 27 75 41 7 89 78 64 39
47 47 70 45 23 65 3 41 44
87 13 82 38 31 12 29 29 80

예제 출력
90
5 7
'''

n = 9
col = 0
row = 0
maxof= [list(map(int, input().split())) for _ in range(n)] # 선언과 동시에 2차원 배열 할당
max_value = maxof[0][0] # max 초기값

for i in range(n):
    for j in range(n):
        if maxof[i][j] > max_value:
            max_value = maxof[i][j]
            col = j
            row = i
print(max_value)
print(row + 1, col + 1)
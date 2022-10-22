'''
완전 탐색 기법

입력
3 4 1 4 9
2 9 4 5 8
9 0 8 2 1
7 0 2 8 4
2 7 2 1 4

출력
3 4 * 4 9 
* 9 4 5 8 
9 0 8 2 * 
7 0 2 8 4 
* 7 2 * 4 

'''
n = 5
map_value = [list(map(int, input().split())) for _ in range(n)]
ins = 0
for i in range(n):
    for j in range(n):
        # 꼭지점일 경우(
            # 1행 1열, 
        if i == 0 and j == 0:
            if (map_value[i][j] < map_value[i][j+1]) and (map_value[i][j] < map_value[i+1][j]):
                map_value[i][j] = -1               
            # 1행 5열, 
        elif i == 0 and j == 4:
            if (map_value[i][j] < map_value[i][j-1]) and (map_value[i][j] < map_value[i+1][j]):
                map_value[i][j] = -1
            # 5행 1열, 
        elif i == 4 and j == 0:
            if (map_value[i][j] < map_value[i-1][j]) and (map_value[i][j] < map_value[i][j+1]):
                map_value[i][j] = -1
            # 5행 5열)
        elif i == 4 and j == 4:
            if (map_value[i][j] < map_value[i-1][j]) and (map_value[i][j] < map_value[i][j-1]):
                map_value[i][j] = -1
        
        # 꼭지점 제외하고 
        # 1행, 
        elif i == 0:
            if (map_value[i][j] < map_value[i][j-1]) and (map_value[i][j] < map_value[i+1][j]) and (map_value[i][j] < map_value[i][j+1]):
                map_value[i][j] = -1
        # 1열, 
        elif j == 0:
            if (map_value[i][j] < map_value[i-1][j]) and (map_value[i][j] < map_value[i][j+1]) and (map_value[i][j] < map_value[i+1][j]):
                map_value[i][j] = -1
        # 5행,
        elif i == 4:
            if (map_value[i][j] < map_value[i][j-1]) and (map_value[i][j] < map_value[i-1][j]) and (map_value[i][j] < map_value[i][j+1]):
                map_value[i][j] = -1
        # 5열 일 경우
        elif j == 4:
            if (map_value[i][j] < map_value[i-1][j]) and (map_value[i][j] < map_value[i][j-1]) and (map_value[i][j] < map_value[i+1][j]):
                map_value[i][j] = -1
        # 가운데 
        else :
            if (map_value[i][j] < map_value[i-1][j]) and (map_value[i][j] < map_value[i][j-1]) and (map_value[i][j] < map_value[i+1][j]) and (map_value[i][j] < map_value[i][j+1]):
                map_value[i][j] = -1

# 출력 부분
for i in range(n):
  for j in range(n):
    if map_value[i][j] == -1:
      print("*", end = ' ')
    else :
      print(map_value[i][j], end = ' ')
  print() 
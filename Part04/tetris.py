'''
완전 탐색 기법

입력
6 7
0 0 0 0 0 0
0 0 0 0 0 0
1 1 1 0 0 1
1 1 1 0 0 1
1 1 1 0 1 1
1 1 1 0 1 1
1 1 1 0 1 1

출력
4 3

'''
# 6, 7
# R = 행
# C => 열

C, R = map(int, input().split())
tetris = [list(map(int, input().split())) for _ in range(R)]
bar = 0
line = 0
x = 0
cc = 0
for mat in tetris:
    if mat.count(1) == C:
        cc+=1
for i in range(C): # 막대가 제일 길게 들어갈 수 있는 곳을 찾자
    count = 0
    for j in range(R):
        if tetris[j][i] == 1: # 1을 만났을 때
            # 1을 처음 만남 -> 막대기 길이의 크기를 잡자
            if bar < j:
                bar = j 
            break
        elif tetris[j][i] == 0 : # 한 번도 1을 만나지 않았을 때
            count+=1
            if count == R : # 한 번도 1을 만나지 않았을 때
                bar = R
            
# 구해진 막대가 어디 어디에 들어갈 수 있을까?
if bar != 0:
    for i in range(C): # 6 -> 열
        flag = True   
        for j in range(bar): 
            if tetris[j][i] == 1: # 바로 아웃
                #print(j,i)
                flag = False
                break   
        if flag : # 한 열에 막대기가 다 들어갈 수 있다
            #print(i)
            mCount = 0
            for k in range(bar): 
                tetris[k][i] = 1
            for mat in tetris:
                if mat.count(1) == C:
                    mCount+=1
            for k in range(bar):
                tetris[k][i] = 0
            if mCount > line :
                line = mCount
                x = i
                
    if line-cc !=0 :        
      print(x+1 ,line-cc)     
    else:
      print('0', '0')
else : # 테트리스가 들어갈 자리가 없어서 쌓지 못하는 경우
    print('0', '0')
    
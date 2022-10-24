'''
완전 탐색 기법

입력
11 12 2 24 10
16 1 13 3 25
6 20 5 21 17
19 4 8 14 9
22 15 7 23 18
5 10 7 16 2
4 22 8 17 13
3 18 1 6 25
12 19 23 14 21
11 24 9 20 15

출력
15

'''
def bingo() :
    bingo = [list(map(int, input().split())) for _ in range(5)] # 빙고판
    bingoNumber = [list(map(int, input().split())) for _ in range(5)] # 빙고 숫자 
    count = 0
    n = 5

    for a in range(5):
        for b in range(5):
            BN = bingoNumber[a][b]
            for i in range(n):
                for j in range(n):
                    if bingo[i][j] == BN:
                        bingo[i][j] = -1 # 빙고 지워주기
                        count += 1
                        
                        cntX = 0    
                        for x in range(n):
                            cnt = 0
                            for y in range(n):
                                if bingo[x][y] == -1:
                                    cnt+=1
                                if cnt == 5: 
                                    cntX +=1
                    
                        for x in range(n):
                            cnt = 0
                            for y in range(n):
                                if bingo[y][x] == -1:
                                    cnt +=1
                                if cnt == 5:
                                    cntX +=1
                
                        if bingo[0][0] == -1 and bingo[1][1] == -1 and bingo[2][2] == -1 and bingo[3][3] == -1 and bingo[4][4] == -1 :
                            cntX +=1
                
                        if bingo[0][4] == -1 and bingo[1][3] == -1 and bingo[2][2] == -1 and bingo[3][1] == -1 and bingo[4][0] == -1 :
                            cntX +=1
                
                        if cntX >= 3:
                            print(count)
                            print(bingo)
                            return 0
                 
if __name__ == "__main__":
        bingo()
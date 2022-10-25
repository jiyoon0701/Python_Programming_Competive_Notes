'''
완전 탐색 기법

입력
4
123 1 1
356 1 0
327 2 0
489 0 1

출력
2

'''
N = int(input())
baseball = [list(map(int, input().split())) for _ in range(N)]
availableCount = 0


for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            flag = False
            if i!=j and j!=k and i!=k : # 다 다르면 
                count = 0
                base_num = str(i*100+j*10+k) # 비교 숫자 
                for x in range(N):
                    bases = str(baseball[x][0]) 
                    strikeCount = 0
                    if base_num[0] == bases[0]:
                        strikeCount+=1
                    if base_num[1] == bases[1] :
                        strikeCount+=1
                    if base_num[2] == bases[2] :
                        strikeCount+=1
                    if strikeCount == baseball[x][1] : # strike 수와 같니?
                        # 그럼 ball을 비교해볼게
                        ballCount = 0        
                        for y in range(3):
                            if base_num.find(bases[y]) >= 0 and base_num.find(bases[y]) != y : # ball 조건
                                ballCount += 1
                        if ballCount == baseball[x][2]:
                                count+=1
                                if count == N:
                                    availableCount+=1
                    else :
                        break

print(availableCount)
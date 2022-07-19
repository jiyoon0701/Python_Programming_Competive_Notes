num = int(input())
gong = [True, False, False]
for i in range(num) :  
    N, M = map(int, input().split())
    if gong[N-1] == True:
        gong[N-1] = False
        gong[M-1] = True
    elif gong[M-1] == True:
        gong[M-1] = False
        gong[N-1] = True

for i in range(len(gong)):
    if gong[i] == True:
        print(i+1)
        break
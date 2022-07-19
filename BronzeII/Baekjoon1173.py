N,m,M,T,R = map(int, input().split())
time = 0 
i = 0
X = m
if m + T > M:
    print(-1)
    N = 0
while time < N:  
    if X + T <= M:
        X += T
        time+=1
    else :
        aa = X - R
        if aa < m:
            X = m
        else : X = aa
    i +=1
if i != 0:
    print(i)
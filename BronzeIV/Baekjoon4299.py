hap, mius = map(int, input().split())
A = (hap + mius) // 2 
B = hap - A 
if mius > hap or (mius + hap)%2 !=0:
    print(-1)
else:
    print(max(A,B), min(A,B))
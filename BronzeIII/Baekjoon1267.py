# 영식 -> 30초마다 10원
# 민식 -> 60초마다 15원
import sys
num = int(sys.stdin.readline())
time = list(map(int, sys.stdin.readline().split()))
Y = 0
M = 0
for i in range(num):
    if time[i] % 29 != 0 :
        Y += time[i] // 30 * 10 + 10
    else :
        Y += time[i] // 30 * 10 + 10
    
for i in range(num):
    if time[i] % 59 != 0 :
        M += time[i] // 60 * 15 + 15
    else :
        M += time[i] // 60 * 15 + 15
        
if Y == M:
    print("Y M {0}" .format(Y))
elif Y > M :
    print("M {0}" .format(M))
else :
    print("Y {0}" .format(Y))
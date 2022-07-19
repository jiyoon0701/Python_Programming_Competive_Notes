import sys

bu = []
for i in range(3) :
    num = int(sys.stdin.readline())
    total = 0
    for j in range(num) :
        numbers = int(sys.stdin.readline())
        total += numbers
    if total == 0:
        bu.append('0')
    elif total < 0 :
        bu.append('-')
    else:
        bu.append('+')
        
for i in range(len(bu)):
    print(bu[i])
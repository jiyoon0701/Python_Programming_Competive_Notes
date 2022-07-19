import sys
num = int(input())
# 제곱 수 1  

for i in range(num) :
    a, b = map(int, input().split())
    a = a % 10 # 나머지
    if a == 0:
        print(10)
    elif a in [1,5,6] :
        print(a)
    elif a in [4, 9] : 
        B = b % 2 # 제곱수를 나눈 나머지
        if B == 0:
            print(a**2%10)
        else :
            print(a)
    else : # 8 2
        B = b % 4
        if B == 0:
            print(a**4 % 10) 
        else:
            print(a**B % 10)
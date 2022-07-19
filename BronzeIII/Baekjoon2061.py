num1, num2 = map(int, input().split())

sieve = [True] * num2
m = int(num2 ** 0.5)
is_o = True

for i in range(2, m + 1):
    if sieve[i] == True :# 소수
        for j in range(i + i, num2, i):
            sieve[j] = False
        
for i in range(2,len(sieve)):
    if sieve[i]:
        if num1 % i == 0:
           is_o = False
           print("BAD", i)
           break

if is_o :
    print("GOOD")        

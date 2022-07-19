P, K = map(int, input().split())
# # k보다 작은 소수로 p가 나누어 떨어지면 좋지 않은 암호, k보다 작은 소수들을 찾자.
# # k보다 작은 소수를 찾았다면 각각의 소수로 p를 나눌 수 있는지 확인하고 그 결과를 출력
is_o = True
sieve = [True] * K
m = int(K ** 0.5)
for i in range(2,m + 1):
    if sieve[i] == True:
        for j in range(i+i, K, i):
            sieve[j] = False

# K보다 작은 소수를 찾았다.
for i in range(2, len(sieve)):
    if sieve[i]: # 소수라면
        if P % (i) == 0:
            is_o = False
            print("BAD", i)
            break
        else :
            is_o = True
            
if is_o :
    print("GOOD")
        
        
        



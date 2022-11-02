
N, M = map(int, input().split())

count2 = 0
count5= 0
for i in range(2,N+1):
  num = i
  while num%2==0 or num%5==0:
    if num%2==0:
      count2 +=1
      num = num//2
    else :
      count5 +=1
      num = num//5

for i in range(2,M+1):
  num = i
  while num%2==0 or num%5==0:
    if num%2==0:
      count2 -=1
      num = num//2
    else :
      count5 -=1
      num = num//5
      
      
for i in range(2,(N-M)+1):
  num = i
  while num%2==0 or num%5==0:
    if num%2==0:
      count2 -=1
      num = num//2
    else :
      count5 -=1
      num = num//5
    
    
print(min(count2,count5))
    
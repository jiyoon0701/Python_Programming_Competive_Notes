'''
입력
10

출력
55

'''

def fibonacci(n):
  fibList=[1, 1]
  if n == 0 : return 0
  if n==1 or n==2:
      return 1
  for i in range(2,n):
      fibList.append( fibList[i-1] + fibList[i-2] )
  return fibList[-1]
  
if __name__ == "__main__":
  n = int(input())
  print(fibonacci(n))
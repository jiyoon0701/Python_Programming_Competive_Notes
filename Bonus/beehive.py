'''
입력
13

출력
3

'''

def bee(num, start, end, i):
  if num >= start and num <= end:
    print(i)
  else :
    start = end + 1
    end = start + (6 * i) -1
    i+=1
    bee(num, start, end, i)
  
if __name__ == "__main__":
  num = int(input())
  start= 1
  end = 1
  i = 1
  bee(num, start, end, i)
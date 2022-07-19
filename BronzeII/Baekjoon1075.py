num = input()
div = int(input())

num = num[:-2] + '00'
num = int(num)

while True:
    if num % div == 0:
        break
    num+=1

num = str(num) 
print(num[-2:])
import sys
num = int(sys.stdin.readline())
result = 0
for i in range(num):
    nums = int(sys.stdin.readline())
    result += nums
print(result -(num-1))
nums = list(map(int, input().split(" ")))
result_num = 0
for i in nums:
    num = i*i
    result_num += num
print(result_num % 10)
    
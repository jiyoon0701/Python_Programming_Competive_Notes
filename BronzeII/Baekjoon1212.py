num = input()
numbers = []
binaryNum1 = format(int(num[0]), 'b')
for i in range(1, len(num)):
    nums = int(num[i])
    binaryNum = format(nums, 'b')
    binaryNum = '{:03d}'.format(int(binaryNum))
    numbers.append(binaryNum)
print(binaryNum1, end = '')
for i in range(len(num)-1):
    print(numbers[i], end = '')
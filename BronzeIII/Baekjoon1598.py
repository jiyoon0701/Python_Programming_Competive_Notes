import math
num1, num2 = map(int, input().split())
A = math.ceil(num1 / 4)
B = math.ceil(num2 / 4)
result =  num1+ (4 * (B - A))
print(abs(result-num2) + abs(B - A))
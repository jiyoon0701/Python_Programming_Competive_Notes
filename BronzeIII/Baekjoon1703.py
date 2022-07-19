A = 1
while True:
    num = list(map(int, input().split()))
    if (num[0] == 0):
        break
    for i in range(1, len(num), 2):
        A = A * num[i] - num[i+1]
    print(A)
    A = 1
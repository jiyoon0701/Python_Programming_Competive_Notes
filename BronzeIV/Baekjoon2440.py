num = int(input())

for i in range(num, 0, -1):
    print("*" * i, end = "")
    for k in range(num, i, -1):
        print("", end = "")
    print()
num = int(input())

for i in range(num - 1, -1, -1):
    print(" "*i, end = "")
    for j in range(num, i, -1):
        print("*",end = "")
    print()
    
        
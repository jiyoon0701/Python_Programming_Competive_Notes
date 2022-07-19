L, P = map(int, input().split())
number = list(map(int, input().split()))

for i in number:
    print("{0}" .format(i - (L*P)), end = " ")
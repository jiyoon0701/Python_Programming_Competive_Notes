while True:
    A = input()
    result = len(A) + 1
    if A == "0" :
        break
    for i in A:
        if i == '1' :
           result += 2
        elif i == '0' :
            result += 4
        else :
            result += 3
    print(result)
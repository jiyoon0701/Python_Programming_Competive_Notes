'''
입력
4 7 10
2 6 18
0 0 0

출력
AP 13
GP 54

'''

def nextNum(number):
    if (number[1] - number[0]) == (number[2] - number[1]):
        answer = f"AP {number[2] + number[1] - number[0]}"
    else:
        answer = f"GP {number[2] * (number[1] // number[0])}"
    return answer


if __name__ == "__main__":
    while True:
        number = list(map(int, input().split()))
        if number == [0, 0, 0]:
            break
        print(nextNum(number))
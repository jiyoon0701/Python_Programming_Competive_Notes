'''
완전 탐색 기법

입력
2
0 0 10 10
2 2 6 6

출력
64
36
'''

def colorpaper():
    n = int(input())
    papers = [list(map(int, input().split())) for _ in range(n)]
    arr = [[0]* 101 for _ in range(101)]
    count = [0] * 100
    for i in range(n): 
        # 시작점에서 끝점까지 색종이 번호로 채우자
        startX = papers[i][0]
        startY = papers[i][1]
        width = papers[i][2]
        height = papers[i][3]
        
        for j in range(startX, startX+width):
            for k in range(startY, startY+height):
                arr[j][k] = i+1 # 색종이 번호
    
    for i in range(101): # 완전 탐색
        for j in range(101):
            count[arr[i][j]] += 1
     
    #숫자 출력
    for i in range(1, n+1):
        print(count[i])   
if __name__ == "__main__":
    colorpaper()
'''
완전 탐색 기법

입력
5
2 3 1 7 3
4 1 9 6 8
5 5 2 4 4
6 5 2 6 7
8 4 2 2 2

출력
4

'''
num = int(input()) # 학생 수
studentCount = [0] * num
students = [list(map(int, input().split())) for i in range(num)]

for i in range(num): # 학생 
    for j in range(num):
        if i == j: # 같은 학생인지 판별
            continue
        elif students[i][0] == students[j][0] or students[i][1] == students[j][1] or students[i][2] == students[j][2] or students[i][3] == students[j][3] or students[i][4] == students[j][4]:
            studentCount[i]+=1
     
maxStudent = max(studentCount)    
print(studentCount.index(maxStudent)+1) 
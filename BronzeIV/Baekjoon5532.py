Bang = list()
for i in range(5):
    Bang.append(int(input()))
Math_day = 0
Korean_day = 0

if Bang[1] % Bang[3] != 0: # 국어
    Korean_day += (Bang[1] // Bang[3])+1
else :
    Korean_day += (Bang[1] // Bang[3])

if Bang[2] % Bang[4] != 0: # 수학
    Math_day += (Bang[2] // Bang[4]) + 1 
else :
    Math_day += (Bang[2] // Bang[4])
    
print(Bang[0] - max(Math_day, Korean_day))

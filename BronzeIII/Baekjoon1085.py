x, y, w, h = map(int, input().split())
width = 0
height = 0
# 가로 - 내가 있는 위치가 중간보다 작다.
if x <= w//2 :
    width = x
else : 
    width = w - x

if y <= h//2 :
    height = y
else : 
    height = h - y

print(min(width, height))

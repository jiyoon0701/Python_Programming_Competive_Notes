result = 0

for i in range(8):
    number = input()
    if i % 2 == 0:
        for i in range(0, 8, 2):
          if number[i] == 'F':
                result+=1
    else :
       for i in range(1, 8, 2):
              if number[i] == 'F':
                result+=1 
    

print(result)
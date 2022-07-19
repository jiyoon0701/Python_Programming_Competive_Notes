import sys
data = {'black' : '0' , 
        'brown' : '1',
        'red' : '2',
        'orange' : '3',
        'yellow' : '4',
        'green' : '5',
        'blue' : '6',
        'violet' : '7',
        'grey' : '8',
        'white' : '9'
        }

color1 = input()
color2 = input()
color3 = input()
result = ''

if color1 in list(data.keys()) :
    result = data.get(color1)

if color2 in list(data.keys()) :
    result = result + data.get(color2)

if color3 in list(data.keys()) :
    if data.get(color3) != '0' :
        result = result + '0' * int(data.get(color3))
    
print(int(result))
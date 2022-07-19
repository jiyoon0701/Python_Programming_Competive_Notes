from concurrent.futures.thread import BrokenThreadPool


moum = []
aa = ['a','e','i','o','u']
while True:
    mun = input().lower()
    if mun != '#':
        cnt = 0 
        for i in mun:
            if i in aa:
                cnt += 1
        moum.append(cnt)
    else:
        break
    
for i in moum:
    print(i)
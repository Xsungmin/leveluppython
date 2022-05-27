M,N = map(int,input().split())
lst = []
for y in range(M):
    for x in range(N):  
        gy = 1+ y*5
        gx = 1+ x*5
        lst.append((gy,gx))

result = [0]*5
arr = [list(input())for _ in range(1+5*M)]

for i in lst:
    y,x = i
    for i in range(3,-1,-1):
        if arr[y+i][x] == '*':
            result[i+1] +=1
            break
        if arr[y][x] == '.':
            result[0] +=1
            break
    
print(*result)


        
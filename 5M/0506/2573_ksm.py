from collections import deque
from sys import stdin

def normal():
    global nn 
    Que = deque()
    Que.append((sy,sx))
    nv[sy][sx] = 1 
    while Que:
        y,x = Que.popleft()
        for dy,dx in [[0,1],[0,-1],[1,0],[-1,0]]:
            ny,nx = y+dy,x+dx
            if nv[ny][nx] == 0 and arr[ny][nx] > 0:
                Que.append((ny,nx))
                nv[ny][nx] = 1
                nn +=1


M,N = map(int, stdin.readline().split())

arr = [ list(map(int, stdin.readline().split()))for _ in range(M)]
cnt = 0


while True:
    
    check = True
    
    while check:
        visited = [[0]*N for _ in range(M)]
        cnt +=1
        QL = 0
        for y in range(1,M-1):
            for x in range(1,N-1):
                if arr[y][x] > 0:
                    QL +=1
                    visited[y][x] = 1
                    for dy,dx in [[0,1],[0,-1],[1,0],[-1,0]]:
                        ny,nx = dy+y,dx+x
                        if visited[ny][nx] == 0 and arr[ny][nx] <= 0 :
                            arr[y][x] -=1
                            if arr[y][x] == 0:
                                QL -=1
                                check = False

    newcheck = True

    for y in range(1,M-1):
        for x in range(1,N-1):
            if arr[y][x] > 0:
                sy = y
                sx = x
                newcheck = False            
                break
        if newcheck == False:
            break



    # print(arr)
    # print(nn,QL)


    
    if newcheck == True:
        cnt =0
        break
    else:
        nv = [[0]*N for _ in range(M)]
        nn = 1
        normal()


    if nn != QL:
        break


print(cnt)

# 62
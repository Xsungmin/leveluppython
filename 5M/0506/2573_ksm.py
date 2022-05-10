from collections import deque
from sys import stdin

def normal():
    global nn 
    nn = 1
    Que = deque()
    Que.append((sy,sx))
    visited[sy][sx] = 2 
    while Que:
        y,x = Que.popleft()
        for dy,dx in [[0,1],[0,-1],[1,0],[-1,0]]:
            ny,nx = y+dy,x+dx
            if visited[ny][nx] != 2 and arr[ny][nx] > 0:
                Que.append((ny,nx))
                visited[ny][nx] = 2
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
        newcheck = True 
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
                    if arr[y][x] > 0:
                        newcheck = False   
                        sy = y
                        sx = x


    if newcheck:
        print(0)
        break
    else:
        normal() 
        if nn != QL: 
            print(cnt)
            break




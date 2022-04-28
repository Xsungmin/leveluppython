from sys import stdin
from collections import deque


def bfs():
    while Q:   
        y,x = Q.popleft()
        for dy,dx in [[0,1],[1,0],[-1,0],[0,-1],[N,0],[-N,0]]:
            ny,nx = y+dy,x+dx
            if dy == N or dy == -N:
                pass
            else: 
                if y // N == ny //N :
                    pass
                else:
                    continue
            if 0<= ny < N*H and 0<= nx < M  and arr[ny][nx] == 0 :
                arr[ny][nx] = arr[y][x] + 1
                Q.append((ny,nx))

M ,N , H = map(int, stdin.readline().split())
arr = [list(map(int, stdin.readline().split())) for _ in range(N*H)]
p = 0
n = 0
cnt = 0
s = -1
Q = deque()
for i in range(N*H):
    for j in range(M):
        if arr[i][j] == 1 :
            Q.append((i,j))
maxv = 0
bfs()
n = 10
for i in range(N*H):
    for j in range(M):
        if arr[i][j] == 0:
            p = 1
        if arr[i][j] > maxv:
            maxv = arr[i][j]        
if p == 1:
    print(-1)

else:
    print(maxv-1)

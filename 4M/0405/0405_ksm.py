def bfs(sx,sy,fx,fy):
    Q = []
    Q.append((sx,sy))
    arr[sx][sy] = 1
    cnt = 0
    while Q:
        x,y = Q.pop(0)
        if x == fx and y == fy :
            return arr[x][y]
        for dx,dy in [[1,2],[2,1],[-1,-2],[-2,-1],[-2,1],[1,-2],[-1,2],[2,-1]]:

            nx,ny = x+dx,y+dy
            if 0<= nx <N and 0<= ny < N and arr[nx][ny] == 0:
                arr[nx][ny] = arr[x][y]+1
                Q.append((nx,ny))
    return 1

T = int(input())
for testcase in range(1,T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    sx, sy = map(int,input().split())
    fx, fy = map(int,input().split())
    
    result = bfs(sx,sy,fx,fy)
    print(result-1)
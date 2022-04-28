from sys import stdin
def change_d(d):
    if d == 0:
        return  3 ,0,-1
    elif d == 1:
        return 0,-1,0
    elif d == 2:
        return 1 ,0,1
    else:
        return  2 ,1,0
def reverse(d):
    if d == 0:
        return  1,0
    elif d == 2:
        return -1,0
    elif d == 1 :
        return 0,-1
    else:
        return 0,1


def clean(y,x,d):
    global cnt
    cnt = 1
    p = 0
    visited[y][x] = 1
    while True:
        nd,dy,dx =change_d(d)
        ny,nx,d = dy+y,dx+x,nd
        if 0<= ny < N and 0<= nx < M and arr[ny][nx] != 1 and visited[ny][nx] == 0: 
            y,x,p = ny,nx,0
            visited[ny][nx] = 1
            cnt +=1
        else:
            p +=1
            if p == 4 :
                sy,sx = reverse(d)
                cy,cx = sy+y,sx+x
                if 0<= cy < N and 0<=cx < M and arr[cy][cx] == 0 :
                    y,x = cy,cx
                    p=0
                else: 
                    return



N, M = map(int,stdin.readline().split())
ry,rx,d = map(int, stdin.readline().split())
arr = [list(map(int, stdin.readline().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]


clean(ry,rx,d)
print(cnt)
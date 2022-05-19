from collections import deque


def bfs(y,x):   # 치즈의 겉부분을 패딩함 
    Q = deque()
    Q.append((y,x))
    arr[y][x] = 2
    while Q:
        y,x = Q.popleft()
        for dy,dx in [[0,1],[1,0],[-1,0],[0,-1]]:
            ny,nx = dy+y,dx+x 
            if 0 <= ny < M and 0 <= nx < N and arr[ny][nx] == 0 :
                arr[ny][nx] = 2
                Q.append((ny,nx))


M,N = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(M)]

# check = False < - 치즈가 하나도 없을 경우 43번째 식과함께 사용 ( 39 지워야함)
check = True
bfs(0,0) # 치즈 겉부분을 패딩하고 시작 
n= 1
cheese = 0
# for y in range(M):  # 만약에 이부분에 걸리면 치즈가 하나도 없는것  < - 예제에는 모두 최소 1개의 치즈가 있다 .
#     for x in range(N):
#         if arr[y][x] == 1:
#             check = True
#             break

while check:
    check = False
    n += 1
    visited = [[0]*N for _ in range(M)]
    for y in range(M): # 치즈 겉부분을 녹임 
        for x in range(N):
            if arr[y][x] == 1:
                cheese += 1
                for dy,dx in [[0,1],[1,0],[-1,0],[0,-1]]:
                    if arr[y+dy][x+dx] == 2 and visited[y+dx][x+dx] == 0:
                        arr[y][x] = 2 
                        visited[y][x] = 1 

    for y in range(M): # 녹인 겉부분이 3이므로 다시 2로 만들어줌
        for x in range(N):
            if arr[y][x] ==3 :
                arr[y][x] = 2



    for y in range(M): # 만약에 구멍이 밖과 만났는지 확인 and 만났다면 bfs로 안을 패딩 
        for x in range(N):
            if arr[y][x] == 0 :
                for dy,dx in [[0,1],[1,0],[-1,0],[0,-1]]:
                    if arr[y+dy][x+dx] == 2 :
                        bfs(y,x) 
            if arr[y][x] == 1:
                check = True
                cheese = 0
                        

print(n-1)
print(cheese)


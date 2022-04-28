from collections import deque

def bfs():
    while queue:
        cz, cy, cx = queue.popleft()
        for dz, dy, dx in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]:
            nz, ny, nx = cz + dz, cy + dy, cx + dx
            if 0 <= nz < H and 0 <= ny < N and 0 <= nx < M and visited[nz][ny][nx] == 0 and arr[nz][ny][nx] == 0:
                visited[nz][ny][nx] = visited[cz][cy][cx] + 1
                queue.append((nz, ny, nx))

def is_zero():
    global check
    for hh in range(H):
        for ii in range(N):
            for jj in range(M):
                if arr[hh][ii][jj] == 0:
                    check = 0
                    return
    check = 1

def ans():
    global check
    max_n = 0
    for hh in range(H):
        for ii in range(N):
            for jj in range(M):
                if visited[hh][ii][jj] == 0 and arr[hh][ii][jj] == 0:
                    return -1
                else:
                    if max_n < visited[hh][ii][jj]:
                        max_n = visited[hh][ii][jj]
    return max_n

# M = 가로, N = 세로, H = 높이
M, N, H = map(int, input().split())
check = 0
# 익은 토마토 = 1, 익지 않은 토마토 = 0, 빈 곳 = -1
arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
visited = [[[0] * M for _ in range(N)] for _ in range(H)]

queue = deque()

for h in range(H):
    for i in range(N):
        for j in range(M):
            if arr[h][i][j] == 1:
                queue.append((h, i, j))
is_zero()
if check == 0:
    bfs()

    print(ans())
else:
    print(0)
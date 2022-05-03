from collections import deque

def bfs(y, x):
    queue = deque()
    queue.append((y, x))

    while queue:
        cy, cx = queue.popleft()
        if abs(ey - cy) + abs(ex - cx) <= 1000:
            return 'happy'
        for i in range(N):
            dy, dx = yx_lst[i]
            if abs(dy - cy) + abs(dx - cx) <= 1000 and visited[i] == 0:
                queue.append((dy, dx))
                visited[i] = 1
    return 'sad'


T = int(input())

for tc in range(T):
    yx_lst = []
    N = int(input())
    visited = [0] * N
    sy, sx = map(int, input().split())
    for _ in range(N):
        py, px = map(int, input().split())
        yx_lst.append((py, px))
    ey, ex = map(int, input().split())

    print(bfs(sy, sx))
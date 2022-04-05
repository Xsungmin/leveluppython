from collections import deque


# (-1, 0), (1, 0), (0, -1), (0, 1)
#    dy = [-2, -1, 1, 2, 2, 1, -1, -2]
#    dx = [1, 2, 2, 1, -1, -2, -2, -1]
def bfs(y, x, ty, tx):

    queue = deque()
    visited[y][x] = 0
    queue.append((y, x))
    while queue:
        cy, cx = queue.popleft()
        if cy == ty and cx == tx:
            return visited[ty][tx]

        for dy, dx in [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]:
            ny, nx = cy + dy, cx + dx
            if 0<=ny<N and 0<=nx<N and visited[ny][nx] == 0:
                visited[ny][nx] = visited[cy][cx] + 1
                queue.append((ny, nx))

T = int(input())
for _ in range(T):
    N = int(input())
    ci, cj = map(int, input().split())
    ti, tj = map(int, input().split())
    visited = [[0] * N for _ in range(N)]



    print(bfs(ci, cj, ti, tj))

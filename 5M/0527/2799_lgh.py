from collections import deque


def bfs(y, x):
    cnt = 1
    q = deque()
    q.append((y, x))
    visited[y][x] = 1
    while q:
        cy, cx = q.popleft()
        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ny = cy + dy
            nx = cx + dx
            if 0 <= ny < (5 * M + 1) and 0 <= nx < (5 * N + 1) and visited[ny][nx] == 0 and arr[ny][nx] == '.':
                cnt += 1
                visited[ny][nx] = 1
                q.append((ny, nx))

    if cnt == 16:
        check[0] += 1
    elif cnt == 12:
        check[1] += 1
    elif cnt == 8:
        check[2] += 1
    else:
        check[3] += 1


M, N = map(int, input().split())

arr = []
for _ in range(5 * M + 1):
    a = list(input())
    arr.append(a)

check = [0] * 5
visited = [[0] * (5 * N + 1) for _ in range(5 * M + 1)]

# bfs를 통해 . 개수를 찾아서 블라인드를 카운트해줌
for i in range(5 * M + 1):
    for j in range(5 * N + 1):
        if arr[i][j] == '.' and visited[i][j] == 0:
            bfs(i, j)

# 총 블라인드 타입은 M*N개 이므로 bfs에 들어가지 않은 전체가 블라인드가 쳐진 집은 따로 더해줌
a = M * N - sum(check)
if a != 0:
    check[4] = a
print(*check)

from collections import deque

# 0을 기준으로 bfs를 돌려 가장자리에 있는 1을 찾아냄
def bfs(y, x):
    global ans
    q = deque()
    q.append((y, x))
    visited[y][x] = 1

    cnt = 0
    while q:
        cy, cx = q.popleft()
        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ny = cy + dy
            nx = cx + dx
            if 0 <= ny < N and 0 <= nx < M and visited[ny][nx] == 0:
                # 만약 0이라면 방문표시하고 0 탐색
                if cheese[ny][nx] == 0:
                    visited[ny][nx] = 1
                    q.append((ny, nx))
                # 1이라면 치즈를 0으로 만들고 방문표시 후 삭제 된 치즈 개수 증가
                elif cheese[ny][nx] == 1:
                    cheese[ny][nx] = 0
                    visited[ny][nx] = 1
                    cnt += 1
    # 삭제한 치즈 개수들을 리스트에 추가
    ans_lst.append(cnt)
    return cnt

N, M = map(int, input().split())

cheese = [list(map(int, input().split())) for _ in range(N)]
visited2 = [[0] * M for _ in range(N)]
ans_lst = []
time = 0

# 전체적으로 돌며 0을 발견하면 bfs를 시작 (방문표시는 처음에 선언하면 방문이 꼬이므로 매 순회마다 방문 초기화)
for i in range(N):
    for j in range(M):
        if cheese[i][j] == 0:
            visited = [[0] * M for _ in range(N)]
            zero = bfs(i, j)
            # 종료 조건
            if zero == 0:
                break
            time += 1

print(time)

# 0이 아닌 최솟값이 가장 마지막에 남은 치즈 개수
ans = 1000000
for i in ans_lst:
    if i != 0 and ans > i:
        ans = i
print(ans)


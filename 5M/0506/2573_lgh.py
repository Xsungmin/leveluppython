from collections import deque


def bfs(y, x):
    queue = deque()
    queue.append((y, x))
    visited2[y][x] = 1
    while queue:
        y, x = queue.popleft()
        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < N and 0 <= nx < M and arr[ny][nx] != 0 and visited2[ny][nx] == 0:
                queue.append((ny, nx))
                visited2[ny][nx] = 1


def find_ice():
    for i in range(N):
        for j in range(M):
            if arr[i][j] != 0:
                ice_lst.append((i, j))
    return


def melting():
    while ice_lst:
        cy, cx = ice_lst.popleft()
        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ny, nx = cy + dy, cx + dx
            if 0 <= ny < N and 0 <= nx < M and arr[ny][nx] == 0:
                visited[cy][cx] += 1

    for i in range(N):
        for j in range(M):
            arr[i][j] = arr[i][j] - visited[i][j]
            visited[i][j] = 0
            if arr[i][j] < 0:
                arr[i][j] = 0

    return


def check():
    cnt = 0

    for i in range(N):
        for j in range(M):
            if arr[i][j] != 0 and visited2[i][j] == 0:
                bfs(i, j)
                cnt += 1
                if cnt == 2:
                    return False
    if cnt == 1:
        for q in range(N):
            for w in range(M):
                if visited2[q][w] != 0:
                    visited2[q][w] = 0
    return True

def check_ice():
    for i in range(N):
        for j in range(M):
            if arr[i][j] != 0:
                return False
    return True


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 빙산 녹는 높이 저장 할 배열
visited = [[0] * M for _ in range(N)]
# bfs에 쓸 방문 배열
visited2 = [[0] * M for _ in range(N)]

ice_lst = deque()
# 만약 처음부터 두덩이로 떨어져있으면 0출력 후 종료
g = check()
if g == False:
    print(0)
    exit()

ans = 0
while True:
    # 반복 할 때마다 빙산 위치 초기화
    ice_lst.clear()
    # 다 녹아서 모두 다 물이면 0 출력
    if check_ice():
        ans = 0
        break
    # 빙산 위치 저장 함수
    find_ice()
    # 빙산 녹이는 함수
    melting()
    # 녹일 때 마다 횟수 1 증가
    ans += 1
    # bfs를 돌려서 1번 이상 돌면 False 후 break
    a = check()
    if a == False:
        break

print(ans)
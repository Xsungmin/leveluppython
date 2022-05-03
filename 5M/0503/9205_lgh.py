from collections import deque

def bfs(y, x):
    queue = deque()
    # 큐에 시작점 저장
    queue.append((y, x))
    while queue:
        cy, cx = queue.popleft()
        # 모든 편의점 비교 후 마지막 편의점과의 거리차이가 1000 이하면 happy
        if abs(ey - cy) + abs(ex - cx) <= 1000:
            return 'happy'
        # 편의점 리스트를 순회하면서 방문하지 않고 거리가 1000 이하면 큐에 append
        for i in range(N):
            dy, dx = yx_lst[i]
            if abs(dy - cy) + abs(dx - cx) <= 1000 and visited[i] == 0:
                queue.append((dy, dx))
                visited[i] = 1
    return 'sad'


T = int(input())

for tc in range(T):
    # 편의점 리스트
    yx_lst = []
    N = int(input())
    # 편의점 방문 리스트
    visited = [0] * N
    # 출발지점
    sy, sx = map(int, input().split())
    for _ in range(N):
        # 편의점 좌표를 리스트에 저장
        py, px = map(int, input().split())
        yx_lst.append((py, px))
    # 끝지점
    ey, ex = map(int, input().split())

    print(bfs(sy, sx))
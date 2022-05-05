from collections import deque
# visited로 각 층을 방문할 수 있는 최소 횟수만을 기록
# q를 다 돈 후 목표지점층의 값 존재 유무에 따라 출력 결과 변경

def bfs():
    q = deque()
    q.append(S)
    while q:
        now = q.popleft()
        up = now + U
        down = now - D
        if 1 <= up <= F:
            if not visited[up] or visited[up] > visited[now] + 1:
                visited[up] = visited[now] + 1
                q.append(up)
        if 1 <= down <= F:
            if not visited[down] or visited[down] > visited[now] + 1:
                visited[down] = visited[now] + 1
                q.append(down)
    if not visited[G]:
        print('use the stairs')
        return
    else:
        print(visited[G]-1)
        return

F, S, G, U, D = map(int, input().split())
visited = [0] * (F+1)
visited[S] = 1 
bfs()
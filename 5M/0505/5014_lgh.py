from collections import deque

'''
총 높이 : F
현재 층 : S
건물 위치 : G
위로 U만큼 : U
아래로 D만큼 : D
'''


def bfs(s):
    queue = deque()
    queue.append(s)
    while queue:
        p_s = queue.popleft()

        # 해당 층 수 찾으면 횟수 return
        if p_s == G:
            return visited[p_s]

        # U, D 0일때를 포함시켜버리면 횟수가 늘어나버리므로 U, D != 0
        # 0층은 존재하지 않으므로 p_s - D 의 최소는 1이 돼야함 (p_s-D > 0)
        # bfs를 통해 가장 먼저 해당 층 수를 찾으면 return
        if p_s + U <= F and visited[p_s + U] == 0 and U != 0:
            visited[p_s + U] = visited[p_s] + 1
            queue.append(p_s + U)

        if p_s - D > 0 and visited[p_s - D] == 0 and D != 0:
            visited[p_s - D] = visited[p_s] + 1
            queue.append(p_s - D)
    # 큐가 비어있으면 엘베 X
    return 'use the stairs'


F, S, G, U, D = map(int, input().split())
# 방문배열
visited = [0] * (F + 1)
# 시작점부터 bfs
print(bfs(S))
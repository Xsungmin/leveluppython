def dfs(cnt, next_i):
    if cnt == M:
        print(*result)
        return
    for i in range(next_i, N):
        if visited[i] == False:
            visited[i] = True
            result.append(i+1)
            dfs(cnt+1, i)
            result.pop()
            visited[i] = False


N, M = map(int, input().split())
visited = [False] * N
result = []
dfs(0, 0)
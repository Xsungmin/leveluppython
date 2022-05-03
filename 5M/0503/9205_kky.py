from collections import deque
import sys
input = sys.stdin.readline

# 거리를 침착하게 구해서 bfs를 잘 적용시키면 쉽게 풀 수 있는문제

def bfs():
    q = deque([])
    q.append(arr[0])
    visited[0] = 1
    while q:
        x, y = q.popleft()
        if abs(arr[-1][0] - x) + abs(arr[-1][1] - y) <= 1000:
            print('happy')
            return
        for i in range(1, n+1):
            n_x, n_y = arr[i]
            if abs(n_x - x) + abs(n_y - y) <= 1000 and not visited[i]:
                q.append(arr[i])
                visited[i] = 1
    print('sad')
    return

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = []
    visited = [0] * (n+1)
    for _ in range(n+2):
        x, y = map(int, input().split())
        arr.append((x, y))
    bfs()
from collections import deque
import sys

def time_3(lst):
    while bomb_lst:
        ci, cj = bomb_lst.popleft()
        lst[ci][cj] = '.'
        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < R and 0 <= nj < C:
                lst[ni][nj] = '.'


R, C, N = map(int, sys.stdin.readline().split())
arr = [list(map(str, sys.stdin.readline().strip())) for _ in range(R)]
bomb_lst = deque()

for i in range(1, N+1):
    if i % 2 == 1:
        time_3(arr)
        for r in range(R):
            for c in range(C):
                if arr[r][c] == 'O':
                    bomb_lst.append((r, c))
    else:
        for r in range(R):
            for c in range(C):
                arr[r][c] = 'O'

for i in range(R):
    ans = ''
    for j in arr[i]:
        ans += j
    print(ans)
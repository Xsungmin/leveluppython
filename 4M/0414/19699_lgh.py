def choice_cows(n, k, m):
    if k == M:
        cnt = 0
        for i in range(2, m+1):
            if m % i == 0:
                cnt += 1
        if cnt == 1:
            if m not in ans:
                ans.add(m)
    for j in range(n, N):
        if used[j] == 0:
            used[j] = 1
            choice_cows(n+1, k+1, cows[j]+m)
            used[j] = 0

import sys


N, M = map(int, sys.stdin.readline().split())
cows = list(map(int, sys.stdin.readline().split()))

select_cow = [0] * M
used = [0] * N

ans = set()
choice_cows(0, 0, 0)


if ans:
    print(*sorted(list(ans)))
else:
    print(-1)
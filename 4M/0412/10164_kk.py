N, M, K = map(int, input().split())
memo = [[1]*M for _ in range(N)]
if K == 0:
    for i in range(1, N):
        for j in range(1, M):
            memo[i][j] = memo[i-1][j] + memo[i][j-1]
    print(memo[N-1][M-1])
else:
    a, b = divmod(K-1, M)
    if (a == 0 and b == M-1) or (a == N-1 and b == 0):
        print(1)
    else:
        for i in range(1, a+1):
            for j in range(1, b+1):
                memo[i][j] = memo[i-1][j] + memo[i][j-1]
        for i in range(a+1, N):
            for j in range(b+1, M):
                memo[i][j] = memo[i-1][j] + memo[i][j-1]
        print(memo[a][b] * memo[N-1][M-1])
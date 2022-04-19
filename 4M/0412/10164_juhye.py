N, M, K = map(int, input().split())
dp = [[1] * (M+1) for _ in range(N+1)]
dp[0][1] = 1
dp[1][0] = 0
if K == 0:
    sol = 1
    for i in range(1, N+1):
        for j in range(1, M+1):
            if i == 1 or j == 1:
                sol = dp[i][j]
            else:
                dp[i][j] = dp[i-1][j]+dp[i][j-1]
                sol = dp[N][M]
    print(sol)
else:
    sol1 = 1
    sol2 = 1
    if K % M == 0:
        ki = K//M
        kj = M
    else:
        ki = (K // M) + 1
        kj = K % M
    # dp[ki][kj] = 1
    for i in range(1, ki+1):
        for j in range(1, kj+1):
            if i == 1 or j == 1:
                dp[i][j] = 1
                sol1 = dp[i][j]
            else:
                dp[i][j] = dp[i-1][j]+dp[i][j-1]
                sol1 = dp[ki][kj]
    dp[ki-1][kj] = 1
    dp[ki][kj-1] = 0
    for a in range(ki+1, N+1):
        for b in range(kj+1, M+1):
            if a == ki or b == kj:
                dp[a][b] = 1
                sol2 = dp[a][b]
            else:
                dp[a][b] = dp[a-1][b]+dp[a][b-1]
                sol2 = dp[N][M]
    print(sol1*sol2)
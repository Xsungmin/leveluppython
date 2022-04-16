def circle(n, m, c):
    if c == 0:
        for i in range(1, n):
            for j in range(1, m):
                lst[i][j] = lst[i - 1][j] + lst[i][j - 1]
        return lst[n-1][m-1]
    else:

        if c == m or c == 1 + m*(c-1):
            return 1

        for i in range(1, circle_y+1):
            for j in range(1, circle_x+1):
                lst[i][j] = lst[i - 1][j] + lst[i][j - 1]

        for i in range(circle_y+1, n):
            for j in range(circle_x+1, m):
                lst[i][j] = lst[i - 1][j] + lst[i][j - 1]

        return lst[circle_y][circle_x] * lst[n-1][m-1]



N, M, C = map(int, input().split())
lst = [[1] * M for _ in range(N)]


circle_y = (C - 1) // M
circle_x = (C - 1) % M
print(circle(N, M, C))

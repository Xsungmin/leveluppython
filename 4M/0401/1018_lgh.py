N, M = map(int, input().split())
board = [list(map(str, input())) for _ in range(N)]
ans = []
for y in range(N-7):
    for x in range(M-7):
        start_W = 0
        start_B = 0
        for r in range(y, y+8):
            for c in range(x, x+8):
                if (r+c) % 2 == 0:
                    if board[r][c] != 'W':
                        start_W += 1
                    if board[r][c] != 'B':
                        start_B += 1
                elif (r+c) % 2 == 1:
                    if board[r][c] == 'W':
                        start_W += 1
                    if board[r][c] == 'B':
                        start_B += 1
        ans.append(start_W)
        ans.append(start_B)

print(min(ans))
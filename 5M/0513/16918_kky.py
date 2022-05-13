from collections import deque
d = [(-1, 0), (1, 0), (0, 1), (0, -1)]
# 구현문제, 짝수 / 홀수에 따라 진행방식이 다르므로 이를 활용
R, C, N = map(int, input().split())
arr = [list(input()) for _ in range(R)]
timer = [[0] * C for _ in range(R)]
q = deque()
for i in range(R):
    for j in range(C):
        if arr[i][j] == 'O':
            timer[i][j] = 1
ans = 1
while ans < N:
    ans += 1
    if ans % 2 == 0:
        for i in range(R):
            for j in range(C):
                if arr[i][j] == '.':
                    arr[i][j] = 'O'
                    timer[i][j] = 0
                else:
                    timer[i][j] += 1
    else:
        for i in range(R):
            for j in range(C):
                if arr[i][j] == 'O':
                    timer[i][j] += 1
                    if timer[i][j] == 3:
                        timer[i][j] = 0
                        arr[i][j] = '.'
                        for di, dj in d:
                            ni = i + di
                            nj = j + dj
                            if 0 <= ni < R and 0 <= nj < C and timer[ni][nj] != 2:
                                arr[ni][nj] = '.'
                                timer[ni][nj] = 0

for i in arr:
    for j in i:
        print(j, end='')
    print()

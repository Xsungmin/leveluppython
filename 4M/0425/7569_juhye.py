# 상자 크기 가로 M, 세로 N, 높이 H
M, N, H = map(int, input().split())
tmt = [list(map(int, input().split())) for _ in range(N*H)]
# print(tmt)
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
cnt = 0
for i in range(N*H):
    for j in range(M):
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            while 0<=ni<N and 0<=nj<M and tmt[i][j] == 1 and tmt[ni][nj] == -1:
                tmt[ni][nj] = 1
                cnt += 1
for i in range(N*H):
    for j in range(M):
        if tmt[i][j] == 1:
            if 0<=i-N<N*H and 0<=i+N<N*H and tmt[i-N][j] == -1 and tmt[i+N][j] == 0:
                tmt[i - N][j] = 1
                tmt[i + N][j] = 1
                cnt += 1
            elif 0<=i-N<N*H and tmt[i-N][j] == 0:
                tmt[i - N][j] = 1
                cnt += 1
            elif 0<=i+N<N*H and tmt[i+N][j] == 0:
                tmt[i + N][j] = 1
                cnt += 1

for i in range(N*H):
    for j in range(M):
        if tmt[i][j] == 0:
            cnt = -1
print(cnt)
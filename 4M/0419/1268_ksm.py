from sys import stdin

N = int(stdin.readline())
arr = [list(map(int,stdin.readline().split())) for _ in range(N)]

narr =[[0]*5 for _ in range(9)]
cnt = [[0] * (N) for _ in range(N) ]

for k in range(N):
    for i in range(5):
        for j in range(N):
            if arr[k][i] == arr[j][i] and k != j:
                cnt[k][j] = 1

min = [1,0]
for i in range(N):
    if min[1] < sum(cnt[i]):
        min = [i+1,sum(cnt[i])]

print(min[0])
N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort(key=lambda x: (-x[1], -x[2], -x[3]))


for i in range(N):
    if arr[i][0] == K:
        cnt = 0
        for j in range(i):
            if arr[i][1:] != arr[j][1:]:
                cnt += 1
        print(cnt+1)
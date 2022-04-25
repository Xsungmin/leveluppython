N = int(input())
idj = [[0] * 1001 for _ in range(1001)]

for k in range(1, N+1):
    j_b, i_b, width, height = list(map(int, input().split()))
    for i in range(j_b, j_b + width):
        for j in range(i_b, i_b+height):
            idj[i][j] = k

for k in range(1, N+1):
    cnt = 0
    for i in range(1001):
        for j in range(1001):
            if idj[i][j] == k:
                cnt += 1
    print(cnt)
# 규칙을 갖는 문제이므로 for문을 활용해 쉽게 풀 수 있다.

M, N = map(int, input().split())
w = [0] * 5
arr = [list(input()) for _ in range(5*M+1)]
for i in range(M):
    c = i*5+1
    for j in range(N):
        r = j*5+1
        cnt = 0
        for k in range(4):
            if arr[c+k][r] == '*':
                cnt += 1
        w[cnt] += 1
print(*w)
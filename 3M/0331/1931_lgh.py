# import sys
# sys.stdin = open('5202_input.txt')

N = int(input())
time = [list(map(int, input().split())) for _ in range(N)]
time.sort(key=lambda x: (x[1], x[0]))

cnt = 0
cur_time = 0
for i in range(N):
    s = time[i][0]
    e = time[i][1]
    if cur_time <= s:
        cnt += 1
        cur_time = e
print(cnt)

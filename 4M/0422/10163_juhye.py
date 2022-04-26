N = int(input()) # 색종이 총 장수
pan = [[0] * 1001 for _ in range(1001)]

for n in range(1, N+1):
    a, b, w, h = map(int, input().split())

    # print(n, a, b, w, h)
    # if n == 1:
    #     sumV = (w-1)*(h-1)
    # else:
    for i in range(a, a+w):
        for j in range(b, b+h):
            # if pan[i][j] == 0:
            #     pan[i][j] = n
            # else:
            pan[j][i] = n

sumV = [0]*(N+1)
for m in range(1, N+1):
    for x in range(1001):
        for y in range(1001):
            if pan[x][y] == m:
                sumV[m] += 1

    print(sumV[m])
#
# # sol = 0
#     for m in range(1, N + 1):
#         sumV = 0
#         for x in range(1001):
#             for y in range(1001):
#                 if pan[x][y] == m:
#                     sumV += 1
#         # for m in range(1, N+1):
#         print(sumV)

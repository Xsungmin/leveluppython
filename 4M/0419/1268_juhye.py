'''
N = int(input())
cls = [list(map(int, input().split())) for _ in range(N)]

maxV = 0
maxi = 0
for k in range(N):
    sumV = 0
    for i in range(N):
        for j in range(N):
            if cls[k][j] == cls[i][j]:
                sumV += 1
    if maxV <= sumV:
        maxV = sumV
        maxi = k+1
print(maxi)
'''
N = int(input()) # 학생 수
cls = [list(map(int, input().split())) for _ in range(N)]

# print(cls)

maxV = -1
lst = [0]*N
for k in range(N):
    sumV = 0
    for i in range(N):
        for j in range(N):
            if k != i:
                if cls[k][j] == cls[i][j]:
                    sumV += 1
    lst[k] = sumV
    for a in lst[:-1]:
        if maxV <= a:
            maxV = a
print(lst.index(maxV)+1)
    # if maxV <= sumV:
    #     maxV = sumV


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

ans_lst = []
for k in range(N):
    lst = [0]*N
    for j in range(5):
        for i in range(N):
            if arr[k][j] == arr[i][j]:
                lst[i] = 1
    ans_lst.append(sum(lst)-5)

print(ans_lst.index(max(ans_lst)) + 1)

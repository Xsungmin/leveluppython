N = int(input())
lst = list(map(int,input().split()))

arr = [0]*N
for j in range(N):
    cnt = 0
    for i in range(N):
        if lst[j] == cnt and arr[i] == 0:
            arr[i] = j+1
            break
        if arr[i] == 0:
            cnt +=1

print(*arr)        
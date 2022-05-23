N = int(input())
lst = list(map(int,input().split()))

arr = [0]*N  # N 개수만큼 arr를 만들어서 

for j in range(N):
    cnt = 0  # 앞에있는 0의 개수
    for i in range(N):
        if lst[j] == cnt and arr[i] == 0: # 앞에있는 개수가 각 키의 값과 같고 그곳이 0이면 그 위치에 추가
            arr[i] = j+1
            break
        if arr[i] == 0: # 아니면 앞에있는 0의 개수를 세어줌
            cnt +=1

print(*arr)        
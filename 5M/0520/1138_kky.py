# 규칙을 찾아내서 구현 완료
# 답을 저장할 리스트를 생성 후 앞에서부터 0개수를 세어가며 일치할 때 자리가 맞는지 판단
n = int(input())
arr = list(map(int, input().split()))
ans = [0] * n
for i in range(1, n+1):
    cnt = 0
    for j in range(n):
        if cnt == arr[i-1]:
            if ans[j] == 0:
                ans[j] = i
                break
            else:
                continue
        if ans[j] == 0:
            cnt += 1
print(*ans)
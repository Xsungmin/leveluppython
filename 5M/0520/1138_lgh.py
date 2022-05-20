N = int(input())
lst = list(map(int, input().split()))
lst_2 = [0] * N

n = 0
# n이 N일 동안
while n != N:
    # 0개수를 셈 (본인보다 큰 숫자가 들어 갈 자리)
    cnt = 0
    for i in range(N):
        # 만약 0의 개수가 본인보다 큰 숫자의 개수이고, 그 자리가 비어있으면
        if cnt == lst[n] and lst_2[i] == 0:
            # 그 자리에 숫자 입력
            lst_2[i] = n + 1
            # n증가 후 break
            n += 1
            break
        # 위 if문에 해당 되지 않고, 0이면 0개수 증가
        if lst_2[i] == 0:
            cnt += 1
print(*lst_2)

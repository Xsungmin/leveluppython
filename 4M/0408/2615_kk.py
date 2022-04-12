def func(y, x):
    # 우상, 우, 우하, 하를 5번 탐색
    for dy, dx in [(-1, 1), (0, 1), (1, 1), (1, 0)]:
        # 진행 반대방향에 같은 돌이 있다면 pass
        if 0 <= y-dy < 19 and 0 <= x-dx < 19 and arr[y][x] == arr[y-dy][x-dx]:
            continue
        # range 고려
        if 0 <= y+4*dy < 19 and 0 <= x+4*dx < 19:
            # 같은 돌의 개수를 카운트
            cnt = 0
            # 우선 4번 탐색
            for i in range(1, 5):
                # 만약 다른 돌을 만날 시 다음 경우의 수 탐색
                if arr[y][x] != arr[y+dy*i][x+dx*i]:
                    break
                # break가 안되면 +1
                cnt += 1
            if cnt == 4:
                # 6목 확인
                if 0 <= y+5*dy < 19 and 0 <= x+5*dx < 19:
                    if arr[y][x] != arr[y+5*dy][x+5*dx]:
                        return True
                else:
                    return True
    return False



arr = [list(map(int, input().split())) for _ in range(19)]
result = 0
# 바둑판 조회
for i in range(19):
    for j in range(19):
        # 0이 아닌 돌을 만날 때(흑 or 백)
        if arr[i][j]:
            ans = func(i, j)
            if ans:
                result = arr[i][j]
                print(result)
                print(i+1, j+1)
                break
    if result:
        break
if not result:
    print(result)
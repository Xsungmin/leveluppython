N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
# 북 0, 동 1, 남 2, 서 3

# 왼쪽 바라보는 방향
turn_dir = [3, 0, 1, 2]
cnt = 0
ans = 0
while True:
    # 청소 횟수 세기
    if arr[r][c] == 0:
        ans += 1

    arr[r][c] = -1
    # 북쪽 바라볼 때
    if d == 0:
        # 먼지, 범위 벗어나지 않았다면
        if arr[r][c - 1] == 0 and 0 <= c - 1:
            # 방향 전환
            d = turn_dir[d]
            # 전진
            c -= 1
            # 회전 횟수 초기화
            cnt = 0
        else:
            d = turn_dir[d]
            cnt += 1

    elif d == 1:
        if arr[r - 1][c] == 0 and 0 <= r - 1:
            d = turn_dir[d]
            r -= 1
            cnt = 0
        else:
            d = turn_dir[d]
            cnt += 1

    elif d == 2:
        if arr[r][c + 1] == 0 and c + 1 < M:
            d = turn_dir[d]
            c += 1
            cnt = 0
        else:
            d = turn_dir[d]
            cnt += 1

    else:
        if arr[r + 1][c] == 0 and r + 1 < N:
            d = turn_dir[d]
            r += 1
            cnt = 0
        else:
            d = turn_dir[d]
            cnt += 1

    # 회전 횟수가 4 이고
    if cnt == 4:
        # 현재 방향의 반대가 벽이면 멈춤
        if d == 0:
            if arr[r + 1][c] == 1:
                break
            else:
                r += 1
                cnt = 0

        elif d == 1:
            if arr[r][c - 1] == 1:
                break
            else:
                c -= 1
                cnt = 0

        elif d == 2:
            if arr[r - 1][c] == 1:
                break
            else:
                r -= 1
                cnt = 0

        else:
            if arr[r][c + 1] == 1:
                break
            else:
                c += 1
                cnt = 0

print(ans)

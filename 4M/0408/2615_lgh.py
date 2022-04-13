def omok():
    # 초기 승리 0으로 설정
    win = 0
    for i in range(19):
        for j in range(19):
            # 바둑알이 있으면
            if arr[i][j] != 0:
                for d in range(4):
                    cnt = 1
                    ni = i + di[d]
                    nj = j + dj[d]
                    while 0 <= ni < 19 and 0 <= nj < 19 and arr[ni][nj] == arr[i][j]:
                        cnt += 1
                        ni += di[d]
                        nj += dj[d]
                        if cnt == 5:
                            # 육목 판정
                            if 0 <= ni < 19 and 0 <= nj < 19 and arr[ni][nj] == arr[i][j]:
                                break
                            if 0 <= i - di[d] < 19 and 0 <= j - dj[d] < 19 and arr[i - di[d]][j - dj[d]] == arr[i][j]:
                                break
                            # 육목이 아니면 초기 발견한 돌의 색깔
                            else:
                                win = arr[i][j]

                            return win, i + 1, j + 1

    return win, 0, 0


arr = [list(map(int, input().split())) for _ in range(19)]
di = [0, 1, 1, -1]
dj = [1, 1, 0, 1]

win, i, j = omok()
if win == 0:
    print(win)
else:
    print(win)
    print(i, j)

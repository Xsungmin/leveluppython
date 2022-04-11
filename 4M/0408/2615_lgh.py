arr = [list(map(int, input().split())) for _ in range(19)]

di = [0, 1, 1, 1]  # 우 대각 하 대각
dj = [1, 1, 0, -1]

win = []
lst = []
no_winner = []
D = 0
flag = 0
for i in range(19):
    for j in range(19):
        if arr[i][j] == 1:
            for d in range(4):
                cnt = 1
                ni = i + di[d]
                nj = j + dj[d]
                while 0 <= ni < 19 and 0 <= nj < 19 and arr[ni][nj] == 1:
                    ni += di[d]
                    nj += dj[d]
                    cnt += 1
                    if cnt == 5:
                        if 0 <= ni < 19 and 0 <= nj < 19:
                            if arr[ni][nj] == 1:
                                no_winner.append(0)
                                flag = 1
                                break
                            if arr[ni-di[d]*6][nj-di[d]*6] == 1:
                                no_winner.append(0)
                                flag = 1
                                break
                        lst.append(i + 1)
                        lst.append(j + 1)
                        win.append(1)
                        flag = 1
                        D = d
                        break

        elif arr[i][j] == 2:
            for d in range(4):
                cnt = 1
                ni = i + di[d]
                nj = j + dj[d]
                while 0 <= ni < 19 and 0 <= nj < 19 and arr[ni][nj] == 2:
                    ni += di[d]
                    nj += dj[d]
                    cnt += 1
                    if cnt == 5:
                        if 0 <= ni < 19 and 0 <= nj < 19:
                            if arr[ni][nj] == 2:
                                no_winner.append(0)
                                flag = 1
                                break
                            if arr[ni-di[d]*6][nj-di[d]*6] == 2:
                                no_winner.append(0)
                                flag = 1
                                break
                        lst.append(i + 1)
                        lst.append(j + 1)
                        win.append(2)
                        flag = 1
                        break
    if flag == 1:
        break

if lst:
    if D == 3:
        print(win[0])
        print(lst[0] + 4, lst[1] - 4)
    else:
        print(win[0])
        print(lst[0], lst[1])

else:
    print(no_winner[0])

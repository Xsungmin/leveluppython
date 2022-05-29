T = int(input())
for tc in range(T):
    go = input()
    # 앞 뒤 왼 오
    d_lst = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    cx = 0
    cy = 0
    cx_lst = [0]
    cy_lst = [0]
    d = 0
    # d에 맞춰 방향을 전환
    for i in go:
        # 해당 방향으로 전진 ( += )
        if i == 'F':
            dx, dy = d_lst[d]
            cx += dx
            cy += dy
            cx_lst.append(cx)
            cy_lst.append(cy)
        # 해당 방향으로 후진 ( -= )
        elif i == 'B':
            dx, dy = d_lst[d]
            cx -= dx
            cy -= dy
            cx_lst.append(cx)
            cy_lst.append(cy)
        # 만약 방향을 한바퀴 돌았다면 1로 돌아감
        elif i == 'L':
            if d == 3:
                d = 0
            else:
                d += 1
        # 만약 방향을 한바퀴 돌았다면 -1로 돌아감 (역방향이므로 인덱싱을 -1 부터)
        elif i == 'R':
            if d == -4:
                d = -1
            else:
                d -= 1
    # print(cy_lst)
    # print(cx_lst)
    y1, y2 = max(cy_lst), min(cy_lst)
    x1, x2 = max(cx_lst), min(cx_lst)
    # print(max(cy_lst), min(cy_lst))
    # print(max(cx_lst), min(cx_lst))

    # 초기 리스트에 (0, 0) 좌표를 빼고 계산하면 안됨 오류의 원인
    ans = (y1-y2) * (x1-x2)
    print(ans)
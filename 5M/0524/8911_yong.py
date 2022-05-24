# 조건에 맞춰서 구현하는문제
# 리스트에 로봇이 이동한 좌표를 저장한 후 최대, 최소값을 통해 넓이를 계산
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]

T = int(input())

for _ in range(T):
    M = input()
    My = [0]
    Mx = [0]
    i = 0
    dir = 0
    for _ in M:
        y = My[i]
        x = Mx[i]
        if _ == 'F':
            y += d[dir][0]
            x += d[dir][1]
            My.append(y)
            Mx.append(x)
            i += 1
        elif _ == 'L':
            if dir-1 < 0:
                dir = 3
            else:
                dir -= 1
        elif _ == 'R':
            if dir + 1 > 3:
                dir = 0
            else:
                dir += 1
        elif _ == 'B':
            y -= d[dir][0]
            x -= d[dir][1]
            My.append(y)
            Mx.append(x)
            i += 1
    print(abs(max(My)-min(My))*abs(max(Mx)-min(Mx)))
        

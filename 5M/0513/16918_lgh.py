def find_bomb(lst):
    for i in range(R):
        for j in range(C):
            if lst[i][j] == 'O':
                bomb_lst.append((i, j))

def time_1(lst):
    pass


def time_2(lst):
    for i in range(R):
        for j in range(C):
            lst[i][j] = 'O'


def time_3(lst):
    while bomb_lst:
        ci, cj = bomb_lst.pop(0)
        lst[ci][cj] = '.'
        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < R and 0 <= nj < C:
                lst[ni][nj] = '.'

R, C, N = map(int, input().split())
arr = [list(map(str, input())) for _ in range(R)]
bomb_lst = []
find_bomb(arr)


if N == 1:
    time_1(arr)
elif N % 2 == 0:
    time_2(arr)
elif N % 4 == 3:
    time_2(arr)
    time_3(arr)
elif N > 1 and N % 4 == 1:
    time_2(arr)
    time_3(arr)
    bomb_lst.clear()
    find_bomb(arr)
    time_2(arr)
    time_3(arr)



for i in range(R):
    ans = ''
    for j in arr[i]:
        ans += j
    print(ans)


# 0초는 현재 상태 그대로
# 1초는 모든 공간에 폭탄
# 2초는 아무일 없음
# 3초에 0초에 있던 폭탄들이 터짐


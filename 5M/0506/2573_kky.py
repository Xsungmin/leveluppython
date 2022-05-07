from collections import deque
import sys
input = sys.stdin.readline
# bfs문제 얼음이 있는곳을 저장할 배열과 그 얼음기준 0의 개수를 저장할 배열 2개를 만들어 진행
# 한 타임이 지날때마다 얼음이 분리되었는지 혹은 다 녹았는지를 판단하는 함수도 생성
# 과정을 줄일 수 있을거같은 느낌...

d = [(0, 1), (1, 0), (-1, 0), (0, -1)]

# 방문배열 생성 후 q에 있는 값으로 bfs진행
# 만약 돌린 후에 q의 인덱스를 참조해 방문표시가 안된 부분이 있다면 빙하가 갈라진 것
def check():
    visited = [[0] * M for _ in range(N)]
    check_q = deque()
    check_q.append(q[0])
    visited[q[0][0]][q[0][1]] = 1
    while check_q:
        y, x = check_q.popleft()
        for dy, dx in d:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < N and 0 <= nx < M and arr[ny][nx] and not visited[ny][nx]:
                visited[ny][nx] = 1
                check_q.append((ny, nx))
    for i in q:
        if visited[i[0]][i[1]] == 0:
            return True
    return False

# 주변에 q를 pop하여 해당 인덱스 주변에 얼음이 없는(=0) 곳을 카운트
def bfs():
    cnt = 1
    zero_val = deque()
    while True:
        while q:
            y, x = q.popleft()
            val = 0
            for dy, dx in d:
                ny = y + dy
                nx = x + dx
                if 0 <= ny < N and 0 <= nx < M and not arr[ny][nx]:
                    val += 1
            zero_val.append((y, x, val))
        # 만들어진 zero_val을 pop하며 얼음을 녹이고 만약 얼음이 0이 아니라면 다시 q에 추가
        while zero_val:
            y, x, val = zero_val.popleft()
            arr[y][x] -= val
            if arr[y][x] <= 0:
                arr[y][x] = 0
            else:
                q.append((y, x))
        # 한 사이클마다 빙하가 갈라졌는지 체크
        if q:
            if check():
                return cnt
        # q가 비어있다면 빙하가 다 녹은거임
        else:
            return 0
        cnt += 1

# 얼음이 있는곳을 모두 저장
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
q = deque()
for i in range(N):
    for j in range(M):
        if arr[i][j]:
            q.append((i, j))
print(bfs())
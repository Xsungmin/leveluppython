from sys import stdin
import math

def so(a):
    for i in range(2,a):
        if a % i == 0:
            return False
    return True # 소수


def is_prime(number):
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


N, M = map(int,stdin.readline().split())
lst = list(map(int,stdin.readline().split()))


lst2 = [] # 중복값확인
V = [] # dfs
def dfs(depth):
    if depth == M :
        # 종료 조건 후 처리하는 일 : 더하고, 소수판별하고 정답에 더해주기
        result = sum(V)
        if is_prime(result) and result not in lst2:
            lst2.append(result)
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            V[depth] = lst[i]
            dfs(depth + 1)
            visited[i] = False

V = [0] * M
visited = [False] * N
dfs(0)

if lst2:
    lst2.sort()
    print(*lst2)

else:
    print(-1)
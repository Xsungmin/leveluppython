'''
3
8
0 0
7 0
100
0 0
30 50
10
1 1
1 1
'''

def bfs(si, sj, mi, mj):
    queue = []              # 큐 생성
    queue.append((si, sj))    # 시작점 인큐
    chess[si][sj] = 1       # 시작점 방문표시
    while queue:            # 큐가 비어있지 않으면 반복
        si, sj = queue.pop(0)     # t<-디큐
        if si == mi and sj == mj:   # 목적지에 도착했으면
            return print(chess[mi][mj] -1) # 이동 칸수 
        for di, dj in [[-2,-1],[-2,1],[-1,2],[1,2],[2,1],[2,-1],[1,-2],[-1,-2]]:  # 이동할 수 있는 칸
            ni, nj = si+di, sj+dj         # 주변 칸 좌표
            if 0<=ni<L and 0<=nj<L and chess[ni][nj] ==0: # 체스판을 벗어나지 않고, 인접이면서 방문하지 않은 곳 조건
                queue.append((ni,nj))   # 인접하고, 방문하지 않은 정점 인큐
                chess[ni][nj] = chess[si][sj] + 1 # 한 칸 더 지나옴 (칸 수)

T = int(input())
for tc in range(1, T+1):
    L = int(input()) # 체스판 한변의 길이
    si, sj = map(int, input().split())  # 시작점
    mi, mj = map(int, input().split())  # 도착점

    chess = [[0]*L for _ in range(L)] # 빈 체스판
    bfs(si, sj, mi, mj)






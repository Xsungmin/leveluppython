# 1~N 자연수 중 중복 없이 M개 수열 (오름차순)
# 처음 코드: 백트래킹 순열 코드를 참고해서 작성했다.
# 처음에 p[s]=i로 구현해봤으나 원소가 N개가 출력되어 M개 출력을 위해 p를 빈 리스트로 만들고 append와 pop을 이용했다.

def sol(s):
    if s==M: # 순열 완성
        if p == sorted(p): # 오름차순 정렬
            print(*p)
        return
    else:
        for i in range(N):
            if not visited[i]: # 방문 안 한 원소에 대해
                p.append(lst[i]) # 해당 원소 빈 리스트에 추가
                visited[i] = True # 방문 표시
                sol(s+1)
                p.pop() # 복구
                visited[i] = False # 방문 상태 되돌리기

N, M = map(int, input().split())
visited = [False]*(N)
lst = []
for x in range(1, N+1): # 1~N 집합 리스트를 만들어줌
    lst.append(x)
p = []
sol(0)
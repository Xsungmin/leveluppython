from sys import stdin

def so(a):
    if a ==2 or a==3:
        return True
    for i in range(2,a):
        if a % i ==0:
            return False
    return True

N, M = map(int,stdin.readline().split())
lst = list(map(int,stdin.readline().split()))


lst2 = [] # 중복값확인
V = []
visited =[False]*(N)
def dfs(start):
    if len(V)==M :
        # print(V)        
        sumv = sum(V)
        if sumv  not in lst2 :
            if so(sumv) == True:
                lst2.append(sumv)
        return

    for i in range(start,N+1):
        if lst[i-1] and visited[i-1] == False :
            visited[i-1] = True
            V.append(lst[i-1])
            dfs(i+1)
            V.pop()
            visited[i-1] = False
dfs(1)


if lst2:
    lst2.sort()
    print(*lst2)

else:
    print(-1)
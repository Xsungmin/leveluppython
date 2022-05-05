def jul(a): # 절댓값을 만듦
    if a > 0 :
        return a
    else: 
        return -a

def bfs(): # bfs를 돌림
    Q = [start]
    while Q:
        x,y = Q.pop()
        if jul(x-fx)+jul(y-fy) <= 1000: # 도착지점에 닿는지 확인 
            print('happy')
            return 
        for n in range(N):
            nx,ny = ds[n]
            if vistied[n] == 0 and jul(x-nx)+jul(y-ny) <= 1000: # 1000이내이며 인덱스로 방문하지 않은곳
                vistied[n] = 1
                Q.append([nx,ny])
    print('sad')

T = int(input())

for testcase in range(1,T+1):
    N = int(input())
    ds =[]
    start = list(map(int,input().split())) # 시작점 인풋 


    for _ in range(N):                      # 중간점 인풋
        d = list(map(int,input().split()))
        ds.append(d)

    vistied = [0]*N                         # 중간점 개수만큼의 visited

    
    fx,fy =  list(map(int,input().split())) # 도착점인풋
    bfs()

R,C,N = map(int,input().split())
arr = [list(map(str,input())) for _ in range(R)]



if N == 1 :  # 1일경우에 원래 arr를 출력
    for i in arr:
        result = ''
        for j in i:
            result += j
        print(result)


elif N % 2 != 0:

    n= 1 # 홀수인 n= 1 부터 시작해 +2 단위로 저장함
    while n != N:
        newarr =  [['O']*C for _ in range(R)] # newarr를 짝수일때의 값인 모두가 O인 값으로 초기화

        for y in range(R):
            for x in range(C):
                if arr[y][x] == 'O' : # arr에서 O를 찾으면
                    for dx,dy in [[0,1],[0,-1],[1,0],[-1,0],[0,0]]:  # 자기자신과 4방향의 값을 .으로 만든다
                        ny,nx = y+dy, x+dx
                        if 0 <= ny < R and 0<= nx < C :
                            newarr[ny][nx] = '.'
        n += 2

        arr = newarr # new arr를 다시 arr로 저장시키고 2개씩 넘어가면서 탐색

    for i in newarr:
        result = ''
        for j in i:
            result +=j
        print(result)

else:  # 2의 배수인경우 모두 O인 어레이를 출력
    line = 'O'*C
    for i in range(R):        
        print(line)







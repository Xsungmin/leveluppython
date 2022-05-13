R,C,N = map(int,input().split())
arr = [list(map(str,input())) for _ in range(R)]
subarr = [['O']*C for _ in range(R)]






for y in range(R):
    for x in range(C):
        if arr[y][x] == 'O' :
            for dx,dy in [[0,1],[0,-1],[1,0],[-1,0],[0,0]]:
                ny,nx = y+dy, x+dx
                if 0 <= ny < R and 0<= nx < C :
                    subarr[ny][nx] = '.'

if N % 2 == 0 :
    line = 'O'*C
    for i in range(R):        
        print(line)

elif N % 4 == 3:


    for i in subarr:
        result = ''
        for j in i:
            if j == 'O':
                result += '.'
            else:
                result += 'O'
        print(result)

elif N % 4 == 1:
    for i in arr:
        result = ''
        for j in i:
            result += j
        print(result)



arr = [list(map(int, input().split())) for _ in range(19)]
a = 0
def check(i,j):
    global a
    for k in range(1,3):
        if arr[i][j] == k:
            for d1,d2 in [[0,1],[1,0],[1,1],[1,-1]]:
                cnt = 0
                for f in range(1,5):
                    dx,dy = d1*f,d2*f
                    if 0<= i +dx  < 19 and 0<= j+dy <19 and arr[i+dx][j+dy] == k :
                        cnt +=1
                    if cnt != f:
                        break

                if cnt == 4:
                    ni,nj,ki,kj = i-d1,j-d2,i + d1 * 5,j + d2 * 5
                    if ni < 0 or ni > 18  or nj < 0 or  nj > 18  or arr[ni][nj] != k:
                        if (0 <= ki < 19 and 0 <= kj < 19 and arr[ki][kj] != k) or (ki < 0  or ki > 18 or kj < 0 or kj > 18 ) :
                            if d1 == 1 and d2 == -1:
                                print(k)
                                print(i + 5, j - 3)
                            else:
                                print(k)
                                print(i + 1, j + 1)
                            a = 1
                            return

for i in range(19):
    for j in range(19):
        if arr[i][j] == 0:
            continue
        check(i,j)
        if a == 1 :
            break
    if a == 1 :
        break

if a == 0:
    print(0)
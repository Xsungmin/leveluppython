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
                    if i - d1 < 0 or i - d1 > 18  or j - d2 < 0 or  j - d2 > 18  or arr[i - d1][j - d2] != k:
                        if (0 <= i + d1 * 5 < 19 and 0 <= j + d2 * 5 < 19 and arr[i + d1 * 5][j + d2 * 5] != k) or (i + d1 * 5 < 0  or i + d1 * 5 > 18 or j + d2 * 5 < 0 or j + d2 * 5 > 18 ) :
                            if k == 1:
                                if d1 == 1 and d2 == -1:
                                    print(1)
                                    print(i + 5, j - 3)
                                else:
                                    print(1)
                                    print(i + 1, j + 1)
                            else:
                                if d1 == 1 and d2 == -1:
                                    print(2)
                                    print(i + 5, j - 3)
                                else:
                                    print(2)
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
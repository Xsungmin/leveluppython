def check(x,y):
    global min

    #BW 좌표를 
    cnt1 = 0
    cnt2 = 0

    for i in range(8):
        for j in range(8):
            if (i+j) % 2 == 0 :
                if arrs[i+x][j+y] == 0:
                    cnt1 += 1
                if arrt[i+x][j+y] ==0:
                    cnt2 +=1 
            else:
                if arrs[i+x][j+y] == 1:
                    cnt1 += 1
                if arrt[i+x][j+y] ==1:
                    cnt2 +=1

            if cnt1 >= min and cnt2 >= min: # 백트래킹
                return

    if min > cnt1 :
        min = cnt1
    if min > cnt2:
        min = cnt2

S, G = map(int,input().split())
arr = [list(map(str, input())) for _ in range(S)]
arrs = [[0]*G for _ in range(S)]
arrt = [[0]*G for _ in range(S)]

for i in range(S):
    for j in range(G):
        if arr[i][j] == 'B':
            arrs[i][j] = 0
            arrt[i][j] = 1
        else:
            arrs[i][j] = 1
            arrt[i][j] = 0
min = 65 # 바둑판이 64개임
for x in range(S-7): # (1,1) 좌표부터 (S-8)(G-8) 좌표까지 확인
    for y in range(G-7):
        check(x,y)
print(min)

# from sys import stdin
# N = int(stdin.readline())
# arr = [ [0]*1002 for _ in range(1002)]

# for k in range(N):
#     a,b,c,d = map(int,stdin.readline().split())
#     for i in range(c):
#         for j in range(d):
#             arr[b+j][a+i] = k+1

# result= [0]*N

# for y in range(1002):
#     for x in range(1002):
#         for k in range(1,N+1):
#             if arr[y][x] == k:
#                 result[k-1] += 1

# for i in result:
#     print(i)



from sys import stdin
N = int(stdin.readline())

lst = []
x = 0
y = 0
for k in range(N):
    A = list(map(int,stdin.readline().split()))
    lst.append(A)
    if x < A[0]+A[2]:
        x =  A[0]+A[2]
    if y < A[1]+A[3]:
        y = A[1]+A[3]

    
    
arr = [ [0]*(x+1) for _ in range(y+1)]    
 
for k in range(N):     
        for nx in range(lst[k][0],lst[k][0]+lst[k][2]):
            arr[nx][lst[k][1]:lst[k][1]+lst[k][3]] = [k+1]*lst[k][3]

 
result = [0]*N

for ny in range(y):
    for nx in range(x):
        for k in range(1,N+1):
            if arr[ny][nx] == k:
                result[k-1] += 1

for i in result:
    print(i)


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

    
    
arr = [ [0]*x for _ in range(y)]    
 
for k in range(1,N+1):     
        for j in range(lst[k][0],lst[k][0]+lst[k][2]):
            arr[j][lst[k][1]:lst[k][1]+lst[k][3]] = [k]*lst[k][3]

 
result = [0]*N

for ny in range(y):
    for nx in range(x):
        for k in range(1,N+1):
            if arr[ny][nx] == k:
                result[k-1] += 1

for i in result:
    print(i)



# from sys import stdin
# N = int(stdin.readline())

# arr = [[0]*10 for _ in range(10)]

# lst = []
# x = 0
# y = 0
# for k in range(N):
#     A = list(map(int,stdin.readline().split()))
#     lst.append(A)
#     if x < A[0]+A[2]:
#         x =  A[0]+A[2]
#     if y < A[1]+A[3]:
#         y = A[1]+A[3]

# result= [0]*N   
    
# arr = [ [0]*x for _ in range(y)]    
 
# for k in range(N):
#     result[k] = lst[k][2]*lst[k][3]  
#     if sum(lst[k]) == 0:
#         continue
#     for i in range(lst[k][2]):
#         for j in range(lst[k][3]):
#             if  arr[lst[k][1]+j][lst[k][0]+i] == 0 :
#                 arr[lst[k][1]+j][lst[k][0]+i] = k+1
#             else:
#                 result[arr[lst[k][1]+j][lst[k][0]+i]-1] -= 1  
#                 arr[lst[k][1]+j][lst[k][0]+i] = k+1
# for i in result:
#     print(i)
# import copy
# def check(start,f,cnt):
#     global min
#     if cnt >= min:
#         min = cnt
#     mimarr = copy.deepcopy(f)
#     for j in range(lst[start][0],lst[start][1]+1):
        
#         if f[j] == 0:
#             f[j] = 1
#         else:
#             f = mimarr
#             return 
#     for k in range(N):
#         check(k,f,cnt+1)



# N = int(input())
# lst = []
# max = 0
# for _ in range(N):
#     a = list(map(int,input().split()))
#     lst.append(a)
#     if max <a[1]:
#         max = a[1]
# min = 0

# for i in range(len(lst)):
#     arr = [0]*(max+2)
#     check(i,arr,0)
    
# print(min)



N = int(input())
lst = []
for _ in range(N):
    a = list(map(int,input().split()))
    lst.append(a)
# 배운점 : sorted(key=lamda x: x[0])
lst.sort(key=lambda x:x[0])
lst.sort(key=lambda x:x[1])

lt = 0
cnt = 0

for di,dj in lst:
    if di >= lt:
        cnt +=1
        lt = dj

print(cnt)

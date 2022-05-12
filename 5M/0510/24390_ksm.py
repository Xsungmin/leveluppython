# def jori(n):

#     if n == 0:
#         return 0


#     visited = [0]*(time+1)

#     Q = [n]
#     visited[n] = 1

#     while n > 0:
#         n = Q.pop(0)

#         for j in [60,6,3,1]:
#             Nn = n - j

#             if Nn == 0:
#                 return visited[n]
            
#             if 0 <= Nn  and visited[Nn] == 0:
#                 visited[Nn] = visited[n]+1
#                 Q.append(Nn)
            
    

# N,M = map(int,input().split(':'))

# time = N*6 + M//10

# if time <3:
#     print(time+1)

# elif time % 60 < 3:
#     print(time//60 + 1 + (time % 60))
   
# else:
#     cnt = 1
#     joritime = time - 3
#     cnt += jori(joritime)

#     print(cnt)

def jori(n):

    if n == 0:
        return 0

    visited = [0]*(time+1)

    Q = [n]
    visited[n] = 1

    while n > 0:
        n = Q.pop(0)

        for j in [60,6,3,1]:
            Nn = n - j

            if Nn == 0:
                return visited[n]
            
            if 0 <= Nn  and visited[Nn] == 0:
                visited[Nn] = visited[n]+1
                Q.append(Nn)
            
    return 1000
    

N,M = map(int,input().split(':'))

time = N*6 + M//10

# case1 ) 조리중을 나중에
cnt1 = 1
cnt1 += jori(time)        

# case2 ) 조리중을 먼저누름 
cnt = 1
joritime = time - 3

cnt += jori(joritime)



if cnt > cnt1:
    print(cnt1)
else:
    print(cnt)
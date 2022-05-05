# def bfs():
#     Q = []
#     Q.append(S)
#     visited[S] = 1 

#     if S == G :
#         print("0")
#         return 

#     while Q:
#         y = Q.pop(0)
#         for dy in [U,-D]:
#             ny = y +dy 
#             if 1 <= ny <= F and visited[ny] == 0 : 
                
#                 if ny == G:
#                     print(visited[y])
#                     return
                
#                 Q.append(ny)
#                 visited[ny] = visited[y]+1
    
#     print("use the stairs")
#     return 


# F,S,G,U,D = map(int, input().split())
# # S층에서 G층으로 최상층은 F층 U위로U층 D 아래로 d층
# visited = [0]*(F+1)

# bfs()


 # 피드백코드
def bfs():
    Q = []
    Q.append(S)
    visited[S] = 1 

    while Q:
        y = Q.pop(0)

        if y == G:
            print(visited[y]-1)
            return
            
        for dy in [U,-D]:
            ny = y +dy 
            if 1 <= ny <= F and visited[ny] == 0 :                
                Q.append(ny)
                visited[ny] = visited[y]+1
    
    print("use the stairs")
    return 


F,S,G,U,D = map(int, input().split())
# S층에서 G층으로 최상층은 F층 U위로U층 D 아래로 d층
visited = [0]*(F+1)

bfs()

def changeL(lst):
    if lst[0] == 1:
        lst[0] = 0
        lst[1] = 1
    elif lst[0] == -1:
        lst[0] = 0
        lst[1] = -1
    elif lst[1] == 1:
        lst[1] = 0
        lst[0] = -1
    else:
        lst[1] = 0
        lst[0] = 1
    return lst

def changeR(lst):
    if lst[0] == 1:
        lst[0] = 0
        lst[1] = -1
    elif lst[0] == -1:
        lst[0] = 0
        lst[1] = 1
    elif lst[1] == 1:
        lst[1] = 0
        lst[0] = 1
    else:
        lst[1] = 0
        lst[0] = -1
    return lst

def jul(a) :
    if a >= 0 :
        return a
    else:
        return -a

T = int(input())
for testcase in range(T):
    xmax = 0
    xmin = 0
    ymax = 0
    ymin = 0
    
    let = input()

    start = [0,0]
    dis = [-1,0] #북  
    for i in let:
        if i == 'F':
            start[0] += dis[0]
            start[1] += dis[1]
        elif i == 'B':
            start[0] -= dis[0]
            start[1] -= dis[1]            
        elif i == 'L':
            dis = changeL(dis)
        else:
            dis = changeR(dis)
        
        if start[0] > ymax :
            ymax = start[0]
        
        elif start[0] < ymin:
            ymin = start[0]
        
        elif start[1] > xmax:
            xmax = start[1]
        
        elif start[1] < xmin:
            xmin = start[1]
    result = (xmax-xmin) * (ymax-ymin)
    print(result)

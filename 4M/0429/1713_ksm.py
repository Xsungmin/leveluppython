from sys import stdin
N = int(stdin.readline())
S = int(stdin.readline())
vote = list(map(int,stdin.readline().split()))

votenum = [0]*N
votep = [0]*N
voteh = [0]*N
his = 0
for i in vote:
    a = 0
    if i in votep:
        for j in range(N):
            if votep[j] == i:
                votenum[j] +=1
                a = -1
                break

    if a == 0 :        
        for j in range(N):                
            if votenum[j] == 0:
                votep[j] = i
                votenum[j] = 1 
                voteh[j] = his
                his +=1
                a= -1 
                break
    
    if a == 0:
        min = votenum[0]
        delp = 0
        for j in range(N):
            if min > votenum[j]:
                min = votenum[j]
                delp = j
            
            elif min == votenum[j]:
                if voteh[j] < voteh[delp]:
                    delp =  j


        votep[delp] = i
        votenum[delp] = 1
        voteh[delp] = his
        his +=1


votep = list(set(votep))
if votep[0] == 0:
    votep.pop(0)
print(*votep)


            



from sys import stdin

N, K  = map(int,stdin.readline().split())
Nation = []

for i in range(N):
    A = list(map(int,stdin.readline().split()))
    Nation.append(A)
    if A[0] == K:
        KL = A
sum = 0
min_r = 0
max_r = -1

Nation.sort(key=lambda x:x[1],reverse=True)
# print(Nation)
for i in range(N):
    if Nation[i][1] == KL[1]:
        min_r = i
        # print(i ,Nation[i] ,KL,"체크")
        sum += min_r 
        break
for i in range(min_r,N):    
    if Nation[i][1] < KL[1]:
        max_r = i
        # print(i)
        break
if max_r == -1 :
    max_r = N

NationS = Nation[min_r:max_r]
NationS.sort(key=lambda x:x[2],reverse=True)
# print(NationS)
R = max_r - min_r
for i in range(R):
    if NationS[i][2] == KL[2]:
        min_r = i
        # print(i ,NationS[i] ,KL,"체크")
        sum += min_r 
        break
for i in range(min_r,R):    
    if NationS[i][2] < KL[2]:
        max_r = i
        # print(i)
        break
if max_r == -1 :
    max_r = N

NationB = NationS[min_r:max_r]
# print(NationB)


NationB.sort(key=lambda x:x[3],reverse=True)
# print(NationB)
for i in range(len(NationB)):
    if NationB[i][3] == KL[3]:
        sum += i +1
        print(sum)
        break


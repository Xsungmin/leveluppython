# N과 M 15649 번의 풀이를 답으로 그대로 가져왔다 
import copy
def part(s,f,n):
    global l
    if s == f:
        b = copy.deepcopy(l) # l이 sort되면 뒤의 함수 전체가 어그러지므로 깊은복사 1
        l.sort()
        a = copy.deepcopy(l) # 2 lst2에 중복검사를 담기 위해 깊은복사 2
        if a not in lst2: # lst2에 없는 리스트만 복사하게 함 
            lst2.append(a)
            print(*l)
        l = b # l을 다시 sort 전 상태로 초기화 한다.
    else:
        for i in range(n):
            if jae[i] ==0:
                jae[i] = 1
                l[s] = lst[i]
                part(s+1,f,n)
                jae[i] = 0


M,N = map(int,input().split())
lst = []
lst2 = []
for j in range(1,M+1):
    lst.append(j) # M까지의 정수를 채워넣는다
l = [0]*N # 원소의 개수가 N개인 배열을 구하기 위함 
jae = [0]*M 
part(0,N,M)
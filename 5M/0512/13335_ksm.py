from collections import deque
n,w,L = map(int,input().split()) # n -> 다리를 건너는 트럭수 w 다리길이  L 최대하중

truckList = list(map(int,input().split()))
truckNum = [0]*n

bridge = deque([0]*w)
cnt = 0
while truckList:
    cnt +=1
    bridge.popleft()
    if sum(bridge) + truckList[0] <= L:
        bridge.append(truckList[0])
        truckList.pop(0)

    else: 
        bridge.append(0)

cnt += w

print(cnt)

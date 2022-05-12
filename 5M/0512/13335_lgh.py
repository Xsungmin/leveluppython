'''
N이 1이면 팝한 후 while문이 종료 돼버림.
4 2 10
7 4 5 6 예제 일 때

0 7 -> 7 0 -> 0 4 -> 4 5 의 로직으로 가야하는데 아래 코드는
0 7 -> 7 0 -> 0 0 -> 0 4 -> 4 5 의 로직으로 구현 됨..

'''
# N, W, L = map(int, input().split()) # W 길이, L 하중
# trucks = list(map(int, input().split()))

# on = [0] * W
#
# cnt = 0
# while trucks:
#     if sum(on) + trucks[0] <= L:
#         on.pop(0)
#         cnt += 1
#         a = trucks.pop(0)
#         # on.pop(0)
#         on.append(a)
#     else:
#         on.pop(0)
#         on.append(0)
#         cnt += 1
#
# print(cnt)

'''
비어있는 on 배열부터 시작해서 cnt를 1증가 시키고 가장 첫 값을 pop 하면서 if 구문에 들어감
현재 다리의 값과 남아있는 트럭의 가장 첫 값이 하중을 넘지 않으면 on 배열에 더해줌
그렇지 않다면 on 배열 맨 뒤에 0을 넣어줌으로써 앞으로 전진하는 모습을 구현
'''

N, W, L = map(int, input().split()) # W 길이, L 하중
trucks = list(map(int, input().split()))
on = [0] * W

cnt = 0
while trucks:
    cnt += 1
    on.pop(0)
    if sum(on) + trucks[0] <= L:
        a = trucks.pop(0)
        # on.pop(0)
        on.append(a)
    else:
        on.append(0)

# while문은 마지막 트럭이 진입 할 때 종료 됨. 그 후 다리 길이만큼 더한 값을 출력해 줌
print(cnt+W)

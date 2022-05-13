# 매 순간마다 다리에 올라간 트럭의 무게합, 각 트럭이 다리에 있는 시간을 기록하며 진행

n, w, L = map(int, input().split())
t = list(map(int, input().split()))
m = [0] * len(t)
b = []
ans = 1
idx = 0
b.append(idx)
idx += 1
while b:
    ans += 1
    sumV = 0
    remove_lst = []
    for i in b:
        m[i] += 1
        if m[i] == w:
            remove_lst.append(i)
        else:
            sumV += t[i]
    for i in remove_lst:
        b.remove(i)
    if idx < len(t) and sumV + t[idx] <= L:
        b.append(idx)
        idx += 1
print(ans)

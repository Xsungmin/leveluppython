# 괄호 조건에 맞게 조건을 나눠 구현한 문제
# or을 활용하여 ) ]를 한번에 판단이 안돼서 수정
# 함수 선언부의 구조가 중복되기 때문에 단축할 수 있을거같은 문제

def cal(o, v):
    p = 1
    ans = 0
    if V[o] == '(':
        for i in range(o+1, len(V)):
            if visited[i] == 0:
                if V[i] == ')':
                    visited[i] = 1
                    if ans:
                        return v * ans
                    else:
                        return v * p
                elif V[i] == ']':
                    return 0
                elif V[i] == '(':
                    visited[i] = 1
                    val = cal(i, 2)
                    if val:
                        ans += val
                    else:
                        return 0
                elif V[i] == '[':
                    visited[i] = 1
                    val = cal(i, 3)
                    if val:
                        ans += val
                    else:
                        return 0
    else:
        for i in range(o+1, len(V)):
            if visited[i] == 0:
                if V[i] == ']':
                    visited[i] = 1
                    if ans:
                        return v * ans
                    else:
                        return v * p
                elif V[i] == ')':
                    return 0
                elif V[i] == '(':
                    visited[i] = 1
                    val = cal(i, 2)
                    if val:
                        ans += val
                    else:
                        return 0
                elif V[i] == '[':
                    visited[i] = 1
                    val = cal(i, 3)
                    if val:
                        ans += val
                    else:
                        return 0
    return 0

V = list(input())
result = 0
visited = [0] * len(V)
for i in range(len(V)):
    if visited[i] == 0:
        if V[i] == ')' or V[i] == ']':
            result = 0
            break
        elif V[i] == '(':
            visited[i] = 1
            val = cal(i, 2)
            if val:
                result += val
            else:
                result = 0
                break
        elif V[i] == '[':
            visited[i] = 1
            val = cal(i, 3)
            if val:
                result += val
            else:
                result = 0
                break
print(result)
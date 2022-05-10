T = input()

M1 = int(T[0])
M2 = int(T[1])
S1 = int(T[3])

# 10분 누른 횟수 + 1분 누른 횟수
result = M1 + M2

# 만약 초가 30초 이상이면 조리시작 버튼으로 30초 증가시키고(+1), 나머튼지 10초 버튼(S1-3)
if S1 >= 3:
    result += (S1-3) + 1
    print(result)

# 30초 이하면 10초 버튼 누르고 조리시작 버튼
else:
    result += S1 + 1
    print(result)

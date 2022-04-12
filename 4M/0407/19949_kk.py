def func(A, Q, L, S):
    # A : 제출한 답, Q : 문제 번호, L : 3연속 제한, S : 점수
    global result
    # 문제에 대한 답 채점
    if A == arr[Q]:
        S += 1
    # 마지막 문항에서 점수가 5점 이상일 때 결과 1 추가
    if Q == 9 and S >= 5:
        result += 1
        return
    if Q >= 5 and (9 - Q) + S < 5:
        return
    # 5번째 문항 이상일 때, 남은 문항 다 맞춘 점수 + 현재 점수 < 5면 리턴
    for i in range(1, 6):
        # 이전 답과 똑같을 때
        if i == A:
            # 3연속이면 다음 반복문으로
            if L + 1 == 3:
                continue
            # 3연속이 아니면 다음 문항 진행
            func(i, Q+1, L+1, S)
        else:
            # 이전 답과 같지 않으면 L을 1로 초기화
            func(i, Q+1, 1, S)

arr = list(map(int, input().split()))
result = 0
for i in range(1, 6):
    func(i, 0, 1, 0)
print(result)
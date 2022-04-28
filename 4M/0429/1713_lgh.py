# N = 사진틀의 갯수
N = int(input())
rec = int(input())
rec_n = list(map(int, input().split()))
# 사진틀에 포함된 학생
N_lst = []
# 추천 횟수
rec_count = []

# 전체 추천 번호 만큼 순회
for i in range(len(rec_n)):
    flag = 0
    # 만약 사진틀에 이미 학생이 포함 돼 있다면
    if rec_n[i] in N_lst:
        # 사진틀 순회하며
        for c in range(len(N_lst)):
            # 현재 추천 학생의 추천수 1 증가
            if N_lst[c] == rec_n[i]:
                rec_count[c] += 1
                flag = 1
                break
    if flag == 1:
        continue

    # 사진틀이 다 차기 전
    if len(N_lst) < N:
        N_lst.append(rec_n[i])
        rec_count.append(1)
    # 사진틀 다 차면
    else:
        # 추천 수를 순회 하면서
        for j in range(len(rec_count)):
            # 제일 추천이 낮은 학생을 제외시킴
            if rec_count[j] == min(rec_count):
                # 추천이 제일 낮은 학생의 위치를 찾아서
                f = N_lst.index(N_lst[j])
                # 틀에서 삭제, 추천 삭제
                N_lst.pop(f)
                rec_count.pop(f)
                # 현재 학생을 액자와 추천수에 추가
                N_lst.append(rec_n[i])
                rec_count.append(1)
                break
N_lst.sort()
print(*N_lst)
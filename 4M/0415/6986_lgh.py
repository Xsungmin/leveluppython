import sys

N, K = map(int, sys.stdin.readline().split())
scores = []
for _ in range(N):
    score = float(sys.stdin.readline())
    scores.append(score)
scores1 = sorted(scores)
for _ in range(K):
    scores1.pop(0)
    scores1.pop(-1)
ans1 = (sum(scores1) / len(scores1)) + 0.00000001
print(format(ans1, ".2f"))


scores2 = sorted(scores)

for i in range(K):
    scores2[i] = scores2[K]

for i in range(1, K+1):
    scores2[-i] = scores2[-K-1]
ans2 = (sum(scores2) / len(scores2)) + 0.00000001
print(format(ans2, ".2f"))

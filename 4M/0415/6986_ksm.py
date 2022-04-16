from sys import stdin

N, K = map(int, stdin.readline().split())
lst = []
for i in range(N):
    I = float(stdin.readline())
    lst.append(I)

lst.sort()
print(f'{sum(lst[K:N-K])/(N-K*2)+ 0.00000001:.2f}')

for j in range(K):
    lst[j] = lst[K]
    lst[N-j-1] = lst[N-K-1]

print(f'{sum(lst)/N+ 0.00000001:.2f}')
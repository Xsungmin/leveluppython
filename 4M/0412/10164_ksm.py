from sys import stdin
N,M,nu = map(int, stdin.readline().split())
def fac(a):
    f = 1
    for i in range(1,a+1):
        f *= i
    return f
def cho(x,y):
    c = fac(x+y)//(fac(x)*fac(y))
    return c
valx,valy = nu % M,nu//M

if nu == 0:
    print(cho(M-1,N-1))

else:
    rst = cho(valx-1,valy)
    rst2 = cho(M-valx,N-valy-1)

    print(rst*rst2)

# 5 5 20
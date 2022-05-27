
def zero():
    for i in range(1, ((2*s+3))// 2):
        arr[i][start + s+1] = '|'
        arr[i*-1-1][start + s+1] = '|'
        arr[i][start] = '|'
        arr[i*-1-1][start] = '|'
    for i in range(1,s+1):
        arr[0][start + i] = '-'
        arr[(2*s+3)-1][start + i] = '-'

def one():
    for i in range(1, ((2*s+3))// 2):
        arr[i][start+s+1]= '|'
        arr[i*-1-1][start+s+1]='|'

def two():
    for i in range(1, (2*s+3) // 2):
        arr[i][start + s+1] = '|'
        arr[i*-1-1][start] = '|'
    for i in range(1,s+1):
        arr[0][start + i] = '-'
        arr[(2*s+3) // 2][start + i] = '-'
        arr[(2*s+3)-1][start + i] = '-'

def three():
    for i in range(1, (2*s+3) // 2):
        arr[i][start + s+1] = '|'
        arr[i*-1-1][start + s+1] = '|'
    for i in range(1,s+1):
        arr[0][start + i] ='-'
        arr[(2*s+3) // 2][start + i] = '-'
        arr[(2*s+3)-1][start + i] ='-'

def four():
    for i in range(1, (2*s+3) // 2):
        arr[i][start + s+1] = '|'
        arr[i][start] = '|'
        arr[i*-1-1][start + s+1] = '|'
    for i in range(1,s+2-1):
        arr[(2*s+3) // 2][start + i] = '-'

def five():
    for i in range(1, (2*s+3) // 2):
        arr[i][start] = '|'
        arr[i*-1-1][start + s+1] = '|'
    for i in range(1,s+2-1):
        arr[0][start + i] = '-'
        arr[(2*s+3) // 2][start + i] = '-'
        arr[(2*s+3)-1][start + i] = '-'

def six():
    for i in range(1, (2*s+3) // 2):
        arr[i][start] ='|'
        arr[i*-1-1][start] = '|'
        arr[i*-1-1][start + s+1] = '|'
    for i in range(1,s+2-1):
        arr[0][start + i] = '-'
        arr[(2*s+3) // 2][start + i] = '-'
        arr[(2*s+3)-1][start + i] = '-'

def seven():
    for i in range(1, (2*s+3) // 2):
        arr[i][start + s+1] = '|'
        arr[i*-1-1][start + s+ 1] = '|'
    for i in range(1,s+1):
        arr[0][start + i] = '-'

def eigth():
    for i in range(1, (2*s+3) // 2):
        arr[i][start + s+1] = '|'
        arr[i*-1-1][start + s+1] = '|'
        arr[i][start] = '|'
        arr[i*-1-1][start] = '|'
    for i in range(1,s+2-1):
        arr[0][start + i] = '-'
        arr[(2*s+3) // 2][start + i] = '-'
        arr[(2*s+3)-1][start + i] = '-'

def nine():
    for i in range(1, (2*s+3) // 2):
        arr[i][start + s+1] = '|'
        arr[i*-1-1][start + s+ 1] = '|'
        arr[i][start] = '|'
    for i in range(1,s+2-1):
        arr[0][start + i] = '-'
        arr[(2*s+3) // 2][start + i] = '-'
        arr[(2*s+3)-1][start + i] = '-'



s,n = map(str,input().split())
s = int(s)
num = len(n)
arr = [[' ']*(num*(s+3)) for _ in range((2*s+3))]

start = 0

for i in n:
    if i == '0':
        zero()
    elif i == '1':
        one()
    elif i == '2':
        two()
    elif i == '3':
        three()
    elif i == '4':
        four()
    elif i == '5':
        five()
    elif i == '6':
        six()
    elif i == '7':
        seven()
    elif i == '8':
        eigth()
    else :
        nine()
    start += s+2+1

for i in arr:
    word = ''
    for j in i :
        word += j 
    print(word)
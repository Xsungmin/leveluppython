s, n = map(str, input().split())
s = int(s)
l = (2+s) * len(n) 
arr = [[0] * l for _ in range(2*s+3)]
for _ in range(len(n)):
    if n[_] == '1':
        val = _ * (s+2) + s + 1
        for i in range(2*s+3):
            if i != 0 and i != 2*s+2 and i != s+1:
                arr[i][val] = '|'
    elif n[_] == '2':
        val1 = _ * (s+2)
        val2 = _ * (s+2) + s + 1
        for i in range(2*s+3):
            if 0 < i < s+1:
                arr[i][val2] = '|'
            elif s+1 < i < 2*s+2:
                arr[i][val1] = '|'
        for i in range(_ * (s+2), (_+1) * (s+2)):
            if i != _ * (s+2) and i != (_+1) * (s+2) -1:
                arr[0][i] = '-'
                arr[s+1][i] = '-'
                arr[2*s+2][i] = '-'
    elif n[_] == '3':
        for i in range(_ * (s+2), (_+1) * (s+2)):
            if i != _ * (s+2) and i != (_+1) * (s+2) -1:
                arr[0][i] = '-'
                arr[s+1][i] = '-'
                arr[2*s+2][i] = '-'
        val = _ * (s+2) + s + 1
        for i in range(2*s+3):
            if i != 0 and i != 2*s+2 and i != s+1:
                arr[i][val] = '|'
    elif n[_] == '4':
        val1 = _ * (s+2)
        val2 = _ * (s+2) + s + 1
        for i in range(2*s+3):
            if 0 < i < s+1:
                arr[i][val2] = '|'
                arr[i][val1] = '|'
            elif s+1 < i < 2*s+2:
                arr[i][val2] = '|'
        for i in range(_ * (s+2), (_+1) * (s+2)):
            if i != _ * (s+2) and i != (_+1) * (s+2) -1:
                arr[s+1][i] = '-'
    elif n[_] == '5':
        val1 = _ * (s+2)
        val2 = _ * (s+2) + s + 1
        for i in range(2*s+3):
            if 0 < i < s+1:
                arr[i][val1] = '|'
            elif s+1 < i < 2*s+2:
                arr[i][val2] = '|'
        for i in range(_ * (s+2), (_+1) * (s+2)):
            if i != _ * (s+2) and i != (_+1) * (s+2) -1:
                arr[0][i] = '-'
                arr[s+1][i] = '-'
                arr[2*s+2][i] = '-'
    elif n[_] == '6':
        val1 = _ * (s+2)
        val2 = _ * (s+2) + s + 1
        for i in range(2*s+3):
            if 0 < i < s+1:
                arr[i][val1] = '|'
            elif s+1 < i < 2*s+2:
                arr[i][val1] = '|'
                arr[i][val2] = '|'
        for i in range(_ * (s+2), (_+1) * (s+2)):
            if i != _ * (s+2) and i != (_+1) * (s+2) -1:
                arr[0][i] = '-'
                arr[s+1][i] = '-'
                arr[2*s+2][i] = '-'
    elif n[_] == '7':
        val = _ * (s+2) + s + 1
        for i in range(2*s+3):
            if i != 0 and i != 2*s+2 and i != s+1:
                arr[i][val] = '|'
        for i in range(_ * (s+2), (_+1) * (s+2)):
            if i != _ * (s+2) and i != (_+1) * (s+2) -1:
                arr[0][i] = '-'
    elif n[_] == '8':
        val1 = _ * (s+2)
        val2 = _ * (s+2) + s + 1
        for i in range(2*s+3):
            if 0 < i < s+1:
                arr[i][val1] = '|'
                arr[i][val2] = '|'
            elif s+1 < i < 2*s+2:
                arr[i][val1] = '|'
                arr[i][val2] = '|'
        for i in range(_ * (s+2), (_+1) * (s+2)):
            if i != _ * (s+2) and i != (_+1) * (s+2) -1:
                arr[0][i] = '-'
                arr[s+1][i] = '-'
                arr[2*s+2][i] = '-'
    elif n[_] == '9':
        val1 = _ * (s+2)
        val2 = _ * (s+2) + s + 1
        for i in range(2*s+3):
            if 0 < i < s+1:
                arr[i][val1] = '|'
                arr[i][val2] = '|'
            elif s+1 < i < 2*s+2:
                arr[i][val2] = '|'
        for i in range(_ * (s+2), (_+1) * (s+2)):
            if i != _ * (s+2) and i != (_+1) * (s+2) -1:
                arr[0][i] = '-'
                arr[s+1][i] = '-'
                arr[2*s+2][i] = '-'
    elif n[_] == '0':
        val1 = _ * (s+2)
        val2 = _ * (s+2) + s + 1
        for i in range(2*s+3):
            if 0 < i < s+1:
                arr[i][val1] = '|'
                arr[i][val2] = '|'
            elif s+1 < i < 2*s+2:
                arr[i][val1] = '|'
                arr[i][val2] = '|'
        for i in range(_ * (s+2), (_+1) * (s+2)):
            if i != _ * (s+2) and i != (_+1) * (s+2) -1:
                arr[0][i] = '-'
                arr[2*s+2][i] = '-'

for i in arr:
    for j in range(len(i)):
        if i[j] == 0:
            print(' ', end='')
        else:
            print(i[j], end='')
        if j % (s+2) == s+1:
            if j != 0 and j != l:
              print(' ', end='')
    print()
str_s, numbers = map(str, input().split())

s = int(str_s)
next = 0
LCD = [[' '] * (len(numbers) * (s + 3)) for _ in range(2 * s + 3)]
for number in numbers:
    if number == '1':
        for i in range(1, (2 * s + 3) // 2):
            LCD[i][s + 1 + next] = '|'
            LCD[i + s+1][s + 1 + next] = '|'
        next += s + 3
    elif number == '2':
        for i in range(1, (2 * s + 3) // 2):
            LCD[i][s + 1 + next] = '|'
            LCD[i + s+1][next] = '|'
        for i in range(1, s + 1):
            LCD[0][i + next] = '-'
            LCD[(2 * s + 3) // 2][i + next] = '-'
            LCD[((2 * s + 3) - 1)][i + next] = '-'
        next += s + 3
    elif number == '3':
        for i in range(1, (2 * s + 3) // 2):
            LCD[i][s + 1 + next] = '|'
            LCD[i + s+1][s + 1 + next] = '|'
        for i in range(1, s + 1):
            LCD[0][i + next] = '-'
            LCD[(2 * s + 3) // 2][i + next] = '-'
            LCD[((2 * s + 3) - 1)][i + next] = '-'
        next += s + 3
    elif number == '4':
        for i in range(1, (2 * s + 3) // 2):
            LCD[i][s + 1 + next] = '|'
            LCD[i][next] = '|'
            LCD[i + s+1][s + 1 + next] = '|'
        for i in range(1, s + 1):
            LCD[(2 * s + 3) //2 ][i + next] = '-'
        next += s + 3
    elif number == '5':
        for i in range(1, (2 * s + 3) // 2):
            LCD[i][next] = '|'
            LCD[i + s+1][s + 1 + next] = '|'
        for i in range(1, s + 1):
            LCD[0][i + next] = '-'
            LCD[(2 * s + 3) // 2][i + next] = '-'
            LCD[((2 * s + 3) - 1)][i + next] = '-'
        next += s + 3
    elif number == '6':
        for i in range(1, (2 * s + 3) // 2):
            LCD[i][next] = '|'
            LCD[i + s+1][s + 1 + next] = '|'
            LCD[i + s+1][next] = '|'
        for i in range(1, s + 1):
            LCD[0][i + next] = '-'
            LCD[(2 * s + 3) // 2][i + next] = '-'
            LCD[((2 * s + 3) - 1)][i + next] = '-'
        next += s + 3
    elif number == '7':
        for i in range(1, (2 * s + 3) // 2):
            LCD[i][s + 1 + next] = '|'
            LCD[i + s+1][s + 1 + next] = '|'
        for i in range(1, s + 1):
            LCD[0][i + next] = '-'
        next += s+3
    elif number == '8':
        for i in range(1, (2 * s + 3) // 2):
            LCD[i][s + 1 + next] = '|'
            LCD[i][next] = '|'
            LCD[i + s+1][s + 1 + next] = '|'
            LCD[i + s+1][next] = '|'
        for i in range(1, s + 1):
            LCD[0][i + next] = '-'
            LCD[(2 * s + 3) // 2][i + next] = '-'
            LCD[((2 * s + 3) - 1)][i + next] = '-'
        next += s + 3
    elif number == '9':
        for i in range(1, (2 * s + 3) // 2):
            LCD[i][s + 1 + next] = '|'
            LCD[i][next] = '|'
            LCD[i + s+1][s + 1 + next] = '|'
        for i in range(1, s + 1):
            LCD[0][i + next] = '-'
            LCD[(2 * s + 3) // 2][i + next] = '-'
            LCD[((2 * s + 3) - 1)][i + next] = '-'
        next += s + 3
    else:
        for i in range(1, (2 * s + 3) // 2):
            LCD[i][s + 1 + next] = '|'
            LCD[i][next] = '|'
            LCD[i + s+1][s + 1 + next] = '|'
            LCD[i + s+1][next] = '|'
        for i in range(1, s + 1):
            LCD[0][i + next] = '-'
            LCD[((2 * s + 3) - 1)][i + next] = '-'
        next += s + 3

for i in LCD:
    for j in i:
        if j == '-' or '|':
            print(j, end='')
    print()
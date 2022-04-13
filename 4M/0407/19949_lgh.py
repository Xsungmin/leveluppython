ans = [0] + list(map(int, input().split()))
cnt = 0
score = [0]*11
for a in range(1, 6):
    if a == ans[1]:
        score[1] = 1
    else:
        score[1] = 0

    for b in range(1, 6):
        if b == ans[2]:
            score[2] = 1
        else:
            score[2] = 0

        for c in range(1, 6):
            if a == b == c:
                continue
            if c == ans[3]:
                score[3] = 1
            else:
                score[3] = 0

            for d in range(1, 6):
                if b == c == d:
                    continue
                if d == ans[4]:
                    score[4] = 1
                else:
                    score[4] = 0

                for e in range(1, 6):
                    if c == d == e:
                        continue
                    if e == ans[5]:
                        score[5] = 1
                    else:
                        score[5] = 0

                    for f in range(1, 6):
                        if d == e == f:
                            continue
                        if f == ans[6]:
                            score[6] = 1
                        else:
                            score[6] = 0

                        for g in range(1, 6):
                            if e == f == g:
                                continue
                            if g == ans[7]:
                                score[7] = 1
                            else:
                                score[7] = 0

                            for h in range(1, 6):
                                if f == g == h:
                                    continue
                                if h == ans[8]:
                                    score[8] = 1
                                else:
                                    score[8] = 0


                                for i in range(1, 6):
                                    if g == h == i:
                                        continue
                                    if i == ans[9]:
                                        score[9] = 1
                                    else:
                                        score[9] = 0

                                    for j in range(1, 6):
                                        if h == i == j:
                                            continue
                                        if j == ans[10]:
                                            score[10] = 1
                                        else:
                                            score[10] = 0

                                        if sum(score) >= 5:
                                            cnt += 1

print(cnt)
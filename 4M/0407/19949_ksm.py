sol = list(map(int,input().split()))

# def jae(cnt):
#


result = 0
c = [0]*10
for i1 in range(1,6):
    if sol[0] == i1:
        c[0] = 1
    else:
        c[0] = 0
    for i2 in range(1,6):
        if sol[1] == i2:
            c[1] = 1
        else:
            c[1] = 0

        for i3 in range(1,6):
            if i1 == i2 and i1 == i3 :
                continue

            if sol[2] == i3:
                c[2] = 1
            else:
                c[2] = 0

            for i4 in range(1,6):
                if i2 == i3 and i2 == i4 :
                    continue

                if sol[3] == i4:
                    c[3] = 1
                else:
                    c[3] = 0
                for i5 in range(1,6):

                    if i3 == i4 and i3 == i5 :
                        continue
                    if sol[4] == i5:
                        c[4] = 1
                    else:
                        c[4] = 0


                    for i6 in range(1,6):
                        if i4 == i5 and i4 == i6 :
                            continue

                        if sol[5] == i6:
                            c[5] = 1
                        else:
                            c[5] = 0

                        for i7 in range(1,6):
                            if i5 == i6 and i5 == i7 :
                                continue
                            if sol[6] == i7:
                                c[6] = 1
                            else:
                                c[6] = 0

                            for i8 in range(1,6):
                                if i6 == i7 and i6 == i8 :
                                    continue

                                if sol[7] == i8:
                                    c[7] = 1
                                else:
                                    c[7] = 0

                                for i9 in range(1,6):
                                    if i7 == i8 and i7 == i9 :
                                        continue

                                    if sol[8] == i9:
                                        c[8] = 1
                                    else:
                                        c[8] = 0

                                    for i10 in range(1,6):

                                        if i8 == i9 and i8 == i10 :
                                            continue
                                        if sol[9] == i10:
                                            c[9] = 1
                                        else:
                                            c[9] = 0
                                        if sum(c) >= 5:
                                            result +=1


                                            continue


print(result)


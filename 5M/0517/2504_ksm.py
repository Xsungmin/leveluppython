########################################### 브레이크 조건함수 83,89
def check(i):
    global l1,l2,r1,r2
    if string[i] == '(':
        l1 +=1 
    elif string[i] == '[':
        l2 +=1
    elif string[i] == ')':
        r1 +=1
    elif string[i] == ']':
        r2 +=1
##########################################

string = list(map(str,input()))
newstring = [1,2,3]

while len(newstring) > 1 :

    ############################ () , [] 구현    
    newstring = [string[0]]
    for i in range(1,len(string)):
        if len(newstring) > 0 and type(newstring[-1]) == int and type(string[i]) == int:
            number = newstring.pop()
            newstring.append(number + string[i])

        elif string[i-1] == '(' and string[i] == ')':
            newstring.pop()
            if len(newstring) > 0 and type(newstring[-1]) == int:
                number = newstring.pop()
                newstring.append(number + 2)
            else:
                newstring.append(2)

        elif string[i-1] == '[' and string[i] == ']':
            newstring.pop()

            if len(newstring) > 0 and type(newstring[-1]) == int:
                number = newstring.pop()
                newstring.append(number + 3)
            else:
                newstring.append(3)
        else:
            newstring.append(string[i])     



    ###################################### (N) [N] 구현
    string = newstring
    if len(string) > 2 :
        newstring = [string[0],string[1]]

        for i in range(2,len(string)):  
            if string[i-2] == '(' and type(string[i-1]) == int and string[i] == ')':
                newstring.pop()
                newstring.pop()
                if len(newstring) > 0 and type(newstring[-1]) == int:
                    number = newstring.pop()
                    newstring.append(number + 2*string[i-1])
                else:
                    newstring.append(2*string[i-1])        

            elif string[i-2] == '[' and type(string[i-1]) == int and string[i] == ']':
                newstring.pop()
                newstring.pop()
                if len(newstring) > 0 and type(newstring[-1]) == int:
                    number = newstring.pop()
                    newstring.append(number + 3*string[i-1])
                else:  
                    newstring.append(3*string[i-1])       
            else:
                newstring.append(string[i])     
    string = newstring




    ######################################## 종료조건
    l1 = 0 # (
    l2 = 0 # [
    r1 = 0 # )
    r2 = 0 # ]

    check(0)

    for i in range(1,len(string)):
        if (string[i-1] == '(' and string[i] == ']') or (string[i-1] == '[' and string[i] == ')'):
            newstring = [0]
            break
        check(i)

    if (l1-r1 != 0) or (l2-r2 !=0) :
        newstring = [0]
        break

    if len(newstring) == 1:
        if type(newstring[0]) != int :
            newstring = [0]
            break    

print(*newstring)
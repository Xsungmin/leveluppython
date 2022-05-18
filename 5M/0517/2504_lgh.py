arr = input()
stack = []
tmp = 1
acc = 0

for i in range(len(arr)):
    # 여는 괄호 나올때마다 * 2
    if arr[i] == '(':
        tmp *= 2
        stack.append(arr[i])
    elif arr[i] == '[':
        tmp *= 3
        stack.append(arr[i])

    elif arr[i] == ')':
        # 닫는 괄호가 나왔을 때 stack이 비어있거나 짝이 안맞으면
        if not stack or stack[-1] == '[':
            acc = 0
            break
        # 짝이 맞으면 현재까지의 값을 누적
        if arr[i - 1] == '(':
            acc += tmp
        # 짝이 하나 맞았으므로 해당 괄호에 해당하는 값만큼 나눔
        tmp //= 2
        # 계산 된 괄호 제거
        stack.pop()

    else:
        if not stack or stack[-1] == '(':
            acc = 0
            break

        if arr[i - 1] == '[':
            acc += tmp
        tmp //= 3
        stack.pop()

if stack:
    acc = 0
print(acc)

# def check(): # [ 2, 2 ]
#     global lst
#     lst_2 = []
#     while lst:
#         a = lst.pop(0)
#         if not lst_2:
#             lst_2.append(a)
#         else:
#             if len(lst_2) >= 2:
#                 if lst_2[-2] == '(' and type(lst_2[-1]) == int and a == ')':  # ( 2 )
#                     b = lst_2.pop(-1)
#                     lst_2.pop(-1)
#                     lst_2.append(int(b) * 2)
#                 elif lst_2[-2] == '[' and type(lst_2[-1]) == int and a == ']':  # [ 2 ] 2 * 3 - > 6
#                     b = lst_2.pop(-1)
#                     lst_2.pop(-1)
#                     lst_2.append(int(b) * 3)
#
#                 elif type(lst_2[-1]) == int and type(a) == int:
#                     c = int(lst_2[-1]) + int(lst_2[-2])
#                     lst_2.pop(-1)
#                     lst_2.pop(-1)
#                     lst_2.append(c)
#
#                 elif lst_2[-1] == '(' and a == ')':
#                     lst_2.pop(-1)
#                     lst_2.append(2)
#                 elif lst_2[-1] == '[' and a == ']':
#                     lst_2.pop(-1)
#                     lst_2.append(3)
#
#                 elif type(lst_2[-1]) == int and type(a) == int:
#                     b = lst_2.pop(-1)
#                     lst_2.append(int(a) + int(b))
#                 elif a == ')' or a == ']':
#                     if type(lst_2[-1]) == int and type(lst_2[-2]) == int:
#                         c = lst_2.pop(-1)
#                         d = lst_2.pop(-1)
#                         lst_2.append(c+d)
#                         if lst_2[-2] == '(':
#                             lst_2.pop(-2)
#                             e = lst_2.pop()
#                             lst_2.append(int(e) * 2)
#                         elif lst_2[-2] == '[':
#                             e = lst_2.pop()
#                             lst_2.pop(-2)
#                             lst_2.append(int(e) * 2)
#                 else:
#                     lst_2.append(a)
#
#
#             elif len(lst_2) >= 1:
#                 if lst_2[-1] == '(' and a == ')':
#                     lst_2.pop(-1)
#                     lst_2.append(2)
#                 elif lst_2[-1] == '[' and a == ']':
#                     lst_2.pop(-1)
#                     lst_2.append(3)
#                 else:
#                     lst_2.append(a)
#     return lst_2
#
#
# lst = list(input())
#
# arr = check()
# ans = 0
# for i in range(len(arr)):
#     if type(arr[i]) == str:
#         ans = 0
#         break
#     ans += arr[i]
#
# print(ans)
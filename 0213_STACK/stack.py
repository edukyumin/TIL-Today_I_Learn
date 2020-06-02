
####################################################################괄호 판별기
# first = '()((()))'
# second = '((()((((()()((()())((())))))'
# stack = [0] * 20
# top = 0
# x = first
# def check(x):
#     global top , first, second, stack
#     print(stack)
#     for i in range(len(x)):
#         if x[i] == '(':
#             stack[top] = x[i]
#             top += 1
#
#         elif x[i] == ')':
#             stack[top-1] =0
#             top -= 1
#
#     print(stack)
#
#     if top !=0:
#         return False
#
#     else:
#         return True
# print(check(first))
# print(check(second))

# #선생님 코드
# stack = [0]*100
# top = -1
# str = "()((()))"
# wrong = 0
# for i in range(len(str)):
#     if str[i] == '(':
#         top += 1
#         stack[top] = str[i]
#     elif str[i] == ')':
#         if top == -1:
#             wrong = 1
#             break
#         if stack[top] == '(':
#             top -= 1
# if top == -1 and not wrong:
#     print("correct!")
# else:
#     print('wrong!')

#피보나치 두가지방법으로 짜보기
# def fibo(n):
#     print('fibo (',n,') is called')
#     if n<2:
#         return n
#     else:
#         return fibo(n-1) + fibo(n-2)
#
# memo = [0, 1]
#
# def fibo1(n):
#     global memo
#     print('fibo1 (',n,') is called')
#     if n >= 2 and len(memo) <= n:
#         memo.append(fibo1(n-1) + fibo1(n-2))
#     return memo[n]
#
# def fibo2(n):
#     f = [0, 1]
#
#     print('fibo2(',n,') is called')
#     for i in range(2, n + 1):
#         f.append(f[i-1] + f[i-2])
#
#     return f[n]
#
# print('recirsive fibo')
# fibo(7)
#
# print('recursive + memoization fibo')
# fibo1(7)
#
# print('dynamic fibo')
# fibo2(7)

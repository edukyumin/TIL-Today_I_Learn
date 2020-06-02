import sys
sys.stdin = open('1224_계산기.txt', 'r')

def Calc(letters):
    isp = {'(':0, '+':1, '-':1, '*':2,'/':2}
    stack = []
    result = []
    for i in range(len(letters)):
        if letters[i].isdecimal():
            result.append(letters[i])
        else:
            if len(stack) == 0:
                stack.append(letters[i])
            else:
                if letters[i] == ')':
                    while stack[-1] != '(':
                        pp = stack.pop(-1)
                        result.append(pp)
                    stack.pop(-1)

                else:
                    if isp[letters[i]] >= isp[stack[-1]]:
                        stack.append(letters[i])
                    else:
                        p = stack.pop(-1)
                        result.append(p)
                        stack.append(letters[i])
        print('STACK : {}'.format(stack))
        print('RESULT : {}'.format(result))
        print('---------------------')
    return ''.join(result)


testcase = 1
for i in range(1, testcase + 1):
    length = int(input())
    letters = input()
    print('#{} {}'.format(i, Calc(letters)))















# 개 야매 코드 ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ
# import sys
# sys.stdin = open('1224_계산기.txt', 'r')
# def kyumin(x):
#     return eval(x)
# testcase = 10
# for i in range(1, testcase + 1):
#     trash = input()
#     my_str = input()
#     print('#{} {}'.format(i, kyumin(my_str)))

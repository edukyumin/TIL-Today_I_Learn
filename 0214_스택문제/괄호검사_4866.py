import sys
sys.stdin = open('괄호검사_4866.txt', 'r')

def gwa():
    global letters
    stack = [0] * 100
    top = -1
    open = ['(', '{']
    close = [')', '}']
    for i in range(len(letters)):

        if letters[i] in open:
            top += 1
            stack[top] = letters[i]
            # print(stack)
        elif letters[i] in close:
            if top == -1:
                # print(stack)
                return 0
            elif close.index((letters[i])) != open.index(stack[top]):
                return 0
            else:
                stack[top] = 0
                top -= 1
    if top != -1:
        return 0
    return 1

testcase = int(input())
for i in range(1, testcase+1):
    letters = input()
    print('#{} {}'.format(i, gwa()))
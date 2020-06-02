import sys
sys.stdin = open('반복문자지우기_4873.txt', 'r')

def fuc():
    global my_str
    stack = []
    for i in range(len(my_str)):
        if len(stack) == 0:
            stack.append(my_str[i])

        else:
            letter = stack.pop(-1)
            if letter != my_str[i]:
                stack.append(letter)
                stack.append(my_str[i])
            else:
                continue
    return len(stack)

testcase = int(input())
for i in range(1, testcase + 1):
    my_str = input()
    print('#{} {}'.format(i, fuc()))


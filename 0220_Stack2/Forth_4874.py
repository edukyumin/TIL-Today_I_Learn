import sys
sys.stdin = open('Forth_4874.txt', 'r')

def func():
    for i in range(len(letters)):
        if letters[i] == '.':
            if len(letters) == 2:
                return int(letters[0])
            else:
                return 'error'

        else:
            if not letters[i].isdecimal():
                if i - 2 >= 0:
                    if letters[i] == '+':
                        letters[i - 2] = str(int(letters[i-2]) + int(letters[i-1]))
                    elif letters[i] == '-':
                        letters[i - 2] = str(int(letters[i-2]) - int(letters[i-1]))
                    elif letters[i] == '*':
                        letters[i - 2] = str(int(letters[i-2]) * int(letters[i-1]))
                    elif letters[i] == '/':
                        letters[i - 2] = str(int(int(letters[i-2]) / int(letters[i-1])))

                    letters.pop(i-1)
                    letters.pop(i-1)
                    return func()
                else: return 'error'

testcase = int(input())
for i in range(1, testcase + 1):
    letters = list(map(str, input().split()))
    print('#{} {}'.format(i, func()))
import sys

sys.stdin = open('의석이의세로로말해요_5356.txt', 'r')



def selo(letters):
    empty_arr = [['*' for i in range(15)] for i in range(15)]
    result = ''
    for i in range(5):
        for j in range(len(letters[i][0])):
            empty_arr[j][i] = letters[i][0][j]

    for i in range(len(empty_arr)):
        for j in range(len(empty_arr)):
            if empty_arr[i][j] != '*':
                result += empty_arr[i][j]

    return result


testcase = int(input())
for i in range(1, testcase + 1):
    letters = []
    for j in range(5):
        letter = list(map(str, input().split()))
        letters.append(letter)

    print('#{} {}'.format(i, selo(letters)))
import sys
sys.stdin = open('회문_4861.txt', 'r')

def hwe():
    global n, m, letters
    lines = []

    for i in range(n):
        new_str = ''
        lines.append(letters[i])
        lines.append
        for j in range(n):
            new_str += letters[j][i]
        lines.append(new_str)

    for i in range(len(lines)):
        for j in range(n-m+1):
            if lines[i][j:j+m] == lines[i][j:j+m][::-1]:
                return lines[i][j:j+m]


testcase= int(input())
for i in range(1, testcase+1):
    n, m = list(map(int, input().split()))
    letters = [input() for i in range(n)]
    print('#{} {}'.format(i, hwe()))

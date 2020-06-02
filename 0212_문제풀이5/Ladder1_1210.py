import sys
sys.stdin = open('Ladder1_1210.txt', 'r')
def Ladder():
    global arr
    reach = arr[-1].index(2)
    i = 99
    j = reach
    while i > 0:
        if arr[i][j-1] != 1 and arr[i][j+1] != 1:
            i -= 1
        elif arr[i][j - 1] == 1:
            arr[i][j] = 0
            j -= 1
        elif arr[i][j + 1] == 1:
            arr[i][j] = 0
            j += 1
        if i == 0:
            break
    return j-1
testcase = 10
for i in range(1, testcase+1):
    number = int(input())
    arr = [[0]+list(map(int, input().split()))+[0] for i in range(100)]
    print('#{} {}'.format(number, Ladder()))
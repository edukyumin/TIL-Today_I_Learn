import sys
sys.stdin = open('동철이의일분배_1865.txt', 'r')

def work():
    result = []
    for i in range(number):
        for j in range(number):
            gab = 1
            count = 0
            while count <= number:
                gab * arr[i][j]



    return 'end'

testcase = int(input())
for i in range(1, testcase+1):
    number = int(input())
    arr = [list(map(int, input().split())) for i in range(number)]
    print('#{} {}'.format(i, work()))
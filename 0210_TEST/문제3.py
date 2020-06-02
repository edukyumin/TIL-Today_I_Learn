import sys
sys.stdin = open('문제3.txt', 'r')
def third():
    global number, area
    diff = []
    for x in range(1, number):
        for y in range(1, number):
            first, second, third = (0, 0, 0)
            for i in range(0, x):
                for j in range(0, y):
                    first += area[i][j]
            for i in range(x, number):
                for j in range(0, y):
                    second += area[i][j]
            for i in range(0, number):
                for j in range(y, number):
                    third += area[i][j]
            diff.append(max(first, second, third) - min(first, second, third))
    result = min(diff)
    return min(diff)

testcase = int(input())
for i in range(1, testcase+1):
    number = int(input())
    area = [list(map(int, input().split())) for i in range(number)]
    print('#{} {}'.format(i, third()))










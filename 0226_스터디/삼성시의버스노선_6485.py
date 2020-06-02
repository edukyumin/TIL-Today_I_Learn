import sys
sys.stdin = open('삼성시의버스노선_6485.txt', 'r')

def func():
    result = [0] * p
    for i in range(p):
        for j in range(testcase):
            if line[j][0] <= station[i] <= line[j][1]:
                result[i] += 1
    return ' '.join(map(str, result))

T = int(input())
for i in range(1, T+1):
       testcase = int(input())
       line = [list(map(int, input().split())) for _ in range(testcase)]
       p = int(input())
       station = [int(input()) for _ in range(p)]
       print('#{} {}'.format(i, func()))



import sys
sys.stdin = open('5188_최소합.txt', 'r')

def func():
    global arr, N
    dx = [1, 0]
    dy = [0, 1]
    way = ''
    for i in range(N):
        for j in [0, 1]:
            way += str(j)


    return way

tc = int(input())
for i in range(1, tc+1):
    N = int(input())
    arr = [list(map(int, input().split())) for j in range(N)]
    print('#{} {}'.format(i, func()))

import sys
sys.stdin = open("미로의거리_5105.txt")

def func():

    return 0


testcase = int(input())
for i in range(1, testcase+1):
    N = int(input())
    miro = [list(map(int, input().split())) for j in range(N)]
    print('#{} {}'.format(i, func()))
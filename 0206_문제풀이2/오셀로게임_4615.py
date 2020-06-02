import sys
sys.stdin = open('오셀로게임_4615.txt', 'r')

def os():






    return 'end'


testcase = int(input())
for i in range(1, testcase+1):
    n, m = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for i in range(m)]
    print('#{} {}'.format(i, os()))

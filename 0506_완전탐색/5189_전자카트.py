import sys

sys.stdin = open('5189_전자카트.txt', 'r')


def func():
    return 0


tc = int(input())
for i in range(1, tc + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for j in range(N)]
    print('#{} {}'.format(i, func()))

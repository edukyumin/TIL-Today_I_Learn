import sys
sys.stdin = open('5176_이진탐색.txt', 'r')

def tree():

    return 0


testcase = int(input())
for i in range(1, testcase+1):
    E, N = list(map(int, input().split()))
    node = list(map(int, input().split()))
    print('#{} {}'.format(i, tree()))
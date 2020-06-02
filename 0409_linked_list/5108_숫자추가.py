import sys
sys.stdin = open('5108_숫자추가.txt', 'r')

def func():
    global N, M, L, my_list
    for i in range(M):
        where, number = list(map(int, input().split()))
        my_list.insert(where, number)
    return my_list[L]



testcase = int(input())
for i in range( 1, testcase + 1):
    N, M, L = list(map(int, input().split()))
    my_list = list(map(int, input().split()))

    print('#{} {}'.format(i, func()))
import sys
sys.stdin = open('두개의숫자열_1959.txt','r')
def gob():
    global N, M, Aj, Bj
    if N >= M:
        big, small = N, M
        big_list, small_list = Aj, Bj
    else:
        big, small = M, N
        big_list, small_list = Bj, Aj
    result = []

    for i in range(big-small+1):
        x = 0
        for j in range(small):
            y = big_list[i + j] * small_list[j]
            x += y
        result.append(x)

    return max(result)

testcase = int(input())
for i in range(1, testcase + 1):
    N, M = list(map(int, input().split()))
    Aj = list(map(int, input().split()))
    Bj = list(map(int, input().split()))

    print('#{} {}'.format(i, gob()))
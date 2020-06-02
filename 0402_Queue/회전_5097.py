#써큘러 q로 만들거면 한칸 빈칸 필요하다.
import sys
sys.stdin = open('회전_5097.txt', 'r')

def func():
    for i in range(M):
        first = my_q.pop(0)
        my_q.append(first)

    return my_q[0]

testcase = int(input())
for i in range(1, testcase+1):
    N, M = list(map(int, input().split()))
    my_q = list(map(int, input().split()))
    print('#{} {}'.format(i, func()))
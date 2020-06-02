import sys
sys.stdin = open('5178_노드의합.txt', 'r')

def tree():
    node = ['#']*(N+1)
    for i in range(M):
        node[my_list[i][0]] = my_list[i][1]
    my_range = range(N, 0, -1)
    for i in my_range:
        if node[i] == '#':

            try:
                node[i] = node[2*i] + node[2*i+1]
            except IndexError:
                node[i] = node[2*i]
    return node[L]

testcase = int(input())
for i in range(1, testcase+1):
    N, M, L = list(map(int, input().split()))
    my_list = []
    for j in range(M):
        my_list.append(list(map(int, input().split())))
    print('#{} {}'.format(i, tree()))
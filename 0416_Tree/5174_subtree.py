import sys
sys.stdin = open('5174_subtree.txt', 'r')

def tree(N):
    global cnt, node
    for i in range(E):
        if node[i][0] == N:
            cnt += 1
            new = node[i][1]
            tree(new)
    return cnt+1

testcase = int(input())
for i in range(1, testcase+1):
    E, N = list(map(int, input().split()))
    my_list = list(map(int, input().split()))
    cnt = 0
    node = []
    for j in range(E):
        node.append([my_list[2*j], my_list[2*j+1]])
    print('#{} {}'.format(i, tree(N)))
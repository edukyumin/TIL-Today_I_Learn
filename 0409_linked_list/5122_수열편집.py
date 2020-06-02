import sys
sys.stdin = open('5122_수열편집.txt', 'r')

def func():
    global N, M, L, my_list
    for i in range(M):
        new = list(map(str, input().split()))
        if new[0] == 'I':
            my_list.insert(int(new[1]),new[2])
        elif new[0] == 'D':
            my_list.pop(int(new[1]))
        elif new[0] == 'C':
            my_list[int(new[1])] = new[2]

    if len(my_list)>= L:
        return my_list[L]
    else:
        return -1



testcase = int(input())
for i in range( 1, testcase + 1):
    N, M, L = list(map(int, input().split()))
    my_list = list(map(int, input().split()))

    print('#{} {}'.format(i, func()))
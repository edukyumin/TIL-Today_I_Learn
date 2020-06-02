import sys
sys.stdin = open('5120_암호.txt', 'r')

def func():
    global N, M, K, my_list
    start_idx = 0
    for i in range(K):
        start_idx = (start_idx + M) % len(my_list)
        if start_idx == 0:
            my_list.append(my_list[0]+my_list[-1])
            start_idx -=1
        else:
            my_list.insert(start_idx, my_list[start_idx-1] + my_list[(start_idx)%len(my_list)])
    return ' '.join(map(str, my_list[::-1][:10]))


testcase = int(input())
for i in range( 1, testcase + 1):
    N, M, K = list(map(int, input().split()))
    my_list = list(map(int, input().split()))
    print('#{} {}'.format(i, func()))
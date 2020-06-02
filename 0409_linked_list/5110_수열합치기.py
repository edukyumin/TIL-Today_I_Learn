import sys
sys.stdin = open('5110_수열합치기.txt', 'r')

def func():
    global N, M,  my_list
    for i in range(M-1):
        new = list(map(int, input().split()))
        flag = False
        for j in range(len(my_list)):
            if my_list[j] > new[0]:
                my_list[j:0] = new
                flag = True
                break
        if flag == False:
            for k in range(len(new)):
                my_list.append(new[k])

    return ' '.join(map(str, my_list[::-1][0:10]))

testcase = int(input())
for i in range( 1, testcase + 1):
    N, M = list(map(int, input().split()))
    my_list = list(map(int, input().split()))
    print('#{} {}'.format(i, func()))
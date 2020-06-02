import sys
sys.stdin = open('종이붙이기_4869.txt', 'r')

def paper():
    global length
    my_list = [1, 3]
    for i in range(2,length):
        my_list.append(my_list[i-2]*2 + my_list[i-1])
    return my_list[-1]
testcase = int(input())
for i in range(1, testcase+1):
    length = int(input())//10
    print('#{} {}'.format(i, paper()))
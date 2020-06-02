import sys
sys.stdin = open('수의새로운연산_1493.txt','r')
my_list = [1]
d = 0
while my_list[-1] <= 41000:          ### 아웃풋의 최대가 40000쯤 되니깐 이렇게 만들자
    new = my_list[-1] + (1.5+d)
    my_list.append(new)
    d += 1                                   #등차수열을 만듬

def magic(x, y):
    for n in range(len(my_list)):
        if my_list[n] >= x:
            first_diff_1 = my_list[n] - x
            first_diff_2 = my_list[n-1] - x
            if abs(first_diff_1) >= abs(first_diff_2):
                first_diff = -first_diff_2
                nn = n-1
            elif abs(first_diff_1) < abs(first_diff_2):
                first_diff = -first_diff_1
                nn = n
            break

    for m in range(len(my_list)):
        if my_list[m] >= y:
            second_diff_1 = my_list[m] - y
            second_diff_2 = my_list[m-1] - y
            if abs(second_diff_1) >= abs(second_diff_2):
                second_diff = -second_diff_2
                mm = m-1
            elif abs(second_diff_1) < abs(second_diff_2):
                second_diff = -second_diff_1
                mm = m
            break

    sum_diff = first_diff + second_diff
    k = mm+nn+2
    result = my_list[k] + sum_diff
    return int(result)

testcase = int(input())
for i in range(1, testcase + 1):
    x, y = list(map(int, input().split()))
    print('#{} {}'.format(i, magic(x, y)))
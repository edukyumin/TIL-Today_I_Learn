import sys
sys.stdin = open('card.txt', 'r')

testcase = int(input())

for i in range(1, testcase+1):
    number = int(input())
    problems = list(map(str, input().split()))
    empty_list = [0] * 10

    for j in range(number):
        problem = str(problems[0])[j]
        # print(problem, end=' ')
        for k in problem:
            empty_list[int(k)] += 1
    # print(empty_list)

    my_idx = 0
    my_value = 0
    for idx, value in enumerate(empty_list):
        if value == max(empty_list):
            my_idx  = idx
            my_value = value
    print('#%d %d %d' %(i, my_idx, my_value))
    # print('---------')



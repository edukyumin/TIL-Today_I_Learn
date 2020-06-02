import sys
sys.stdin = open('range_sum.txt', 'r')

testcase = int(input())


for i in range(1, testcase + 1):
    read = input()
    read = read.split(' ')
    problem = input()
    problem = problem.split(' ')
    list_number = int(read[0])
    sum_number = int(read[1])
    # print(list_number, sum_number)
    # print(problem)
    result_list = []

    for j in range(list_number-sum_number+1):
        result_sum = 0
        for k in range(sum_number):
            result_sum += int(problem[j + k])
        result_list.append(result_sum)
    # print(result_list)
    max_result = max(result_list)
    min_result = min(result_list)
    print('#%d %d'%(i ,max_result - min_result))



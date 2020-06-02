import sys

sys.stdin = open('min_max.txt', 'r')

testcase = int(input())
# print(testcase)

for k in range(1, testcase+1):
    numbers = int(input())
    problems = list(map(int, input().split()))
    # print(problems)
    for j in range(numbers-1, 0, -1):
        for i in range(j):
            if problems[i] > problems[i+1]:
                 problems[i], problems[i+1] = problems[i+1], problems[i]
    print('#%d %d' %(k, (problems[-1]-problems[0])))

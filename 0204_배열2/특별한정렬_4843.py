import sys
sys.stdin = open('특별한정렬_4843.txt', 'r')

testcase = int(input())

for i in range(1, testcase + 1):
    number = int(input())
    result = []
    numbers = list(map(int, input().split()))
    numbers.sort()

    for j in range(number//2):
        result.append(numbers[-1-j])
        result.append(numbers[0+j])

    result = result[0:10]

    result = list(map(str, result))
    result = ' '.join(result)
    print('#{} {}'.format(i, result))

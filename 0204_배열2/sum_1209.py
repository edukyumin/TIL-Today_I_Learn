import sys
sys.stdin = open('sum_1209.txt', 'r')

testcase = 10


for i in range(1,10+1):
    number = int(input())
    arr = []
    for j in range(100):
        rows = list(map(int, input().split()))
        arr.append(rows)
    # print(i)
    # print(arr)
    result = []

    for x in range(100):
        hap = sum(arr[x])
        result.append(hap)

    result2 = []
    for y in range(100):
        hap2 = 0
        for x in range(100):
            hap2 += arr[x][y]
            result2.append(hap2)

    result3 = []
    for x in range(100):
        result3.append(arr[x][x])

    result4 = []
    for x in range(100):
        result4.append(arr[x][99-x])

    answer =  max(max(result), max(result2), max(result3), max(result4))
    # print(answer)
    print('#{} {}'.format(i, answer))
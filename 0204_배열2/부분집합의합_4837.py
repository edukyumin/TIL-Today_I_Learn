# import sys
# sys.stdin = open('부분집합의합_4837.txt', 'r')

testcase = int(input())

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
n = len(arr)

for t in range(1, testcase+1):
    a, b = map(int, input().split())
    # print(a,b)
    count = 0
    for i in range(1<<n):
        my_arr = []
        for j in range(n):
            if i & (1<<j):
               my_arr.append(arr[j])

        if len(my_arr) == a and sum(my_arr) == b:
            count += 1
    print('#{} {}'.format(t, count))


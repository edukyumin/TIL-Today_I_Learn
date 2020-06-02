import sys
sys.stdin = open('파스칼삼각형_2005.txt', 'r')

def triangle(n):
    my_str = ''
    empty_arr = [[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        empty_arr[i][0] = 1
        empty_arr[i][i] = 1
        if i >= 2:
            for j in range(1,i):
                empty_arr[i][j] = empty_arr[i-1][j-1] + empty_arr[i-1][j]

    for k in empty_arr:
        k = k[0:empty_arr.index(k) + 1]
        k = list(map(str, k))
        result = ' '.join(k)
        my_str += result + '\n'
    return my_str[:-1]

testcase = int(input())
for i in range(1, testcase + 1):
    number = int(input())
    print('#{}\n{}'.format(i, triangle(number)))




#예슬이코드
# tc = int(input())
# for i in range(tc):
#
#     N = int(input())  # 삼각형의 크기
#     lst = [[1] for _ in range(N)]
#
#     for x in range(1, N):
#         for y in range(1, x):
#             lst[x] += [lst[x - 1][y - 1] + lst[x - 1][y]]
#         lst[x] += [1]
#
#     # 출력
#     print('#{}'.format(i + 1))
#
#     for x in range(N):
#         print(' '.join(map(str, lst[x])))
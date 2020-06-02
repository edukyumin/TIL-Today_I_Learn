import sys
sys.stdin = open('coloring_4836.txt', 'r')


testcase = int(input())
for i in range(1, testcase+1):
    empty_arr = [[0 for _ in range(10)] for _ in range(10)]

    number_of_area = int(input())
    arr = []
    for j in range(number_of_area):
        rows = list(map(int,input().split()))
        arr.append(rows)

        if rows[-1] == 1:           #만약 칠하는 색이 빨강이면 a로 대체해준다.
            for x in range(rows[0], rows[2]+1):
                for y in range(rows[1], rows[3]+1):
                    if empty_arr[x][y] == 0 or empty_arr[x][y] == 'a':
                        empty_arr[x][y] = 'a'
                    elif empty_arr[x][y] == 'b':
                        empty_arr[x][y] = 'c'

        elif rows[-1] == 2:
            for x in range(rows[0], rows[2]+1):
                for y in range(rows[1], rows[3]+1):
                    if empty_arr[x][y] ==0 or empty_arr[x][y] == 'b':
                        empty_arr[x][y] = 'b'
                    elif empty_arr[x][y] == 'a':
                        empty_arr[x][y] = 'c'
    # print(empty_arr)
    count = 0
    for x in range(len(empty_arr)):
        for y in range(len(empty_arr[0])):
            if empty_arr[x][y] == 'c':
                count += 1
    print('#{} {}'.format(i, count))



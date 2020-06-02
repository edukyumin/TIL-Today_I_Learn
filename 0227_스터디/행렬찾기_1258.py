import sys
sys.stdin = open('행렬찾기_1258.txt', 'r')

def func():
    result = []
    for i in range(number):
        for j in range(number):
            if arr[i][j] != 0:
                x, y = [1, 1]
                while arr[i+x][j] != 0:
                    x += 1
                while arr[i][j+y] != 0:
                    y += 1
                for a in range(x):
                    for b in range(y):
                        arr[i+a][j+b] = 0

                result.append([x, y])
    result = sorted(result, key = lambda result:(result[0]*result[1], result[0]))
    my_result = [str(len(result))]
    for i in result:
            my_result.append(str(i[0]))
            my_result.append(str(i[1]))
    return ' '.join(my_result)


testcase = int(input())
for i in range(1, testcase+1):
    number = int(input())
    arr = [list(map(int,input().split()))+[0] for i in range(number)]
    arr.append([0]*(number+1))
    print('#{} {}'.format(i, func()))


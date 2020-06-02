import sys
sys.stdin = open('기지국.txt', 'r')

def tel():
    abc = ['A', 'B', 'C']
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    for i in range(3,number+3):
        for j in range(3,number+3):
            if arr[i][j] == 'A':
                for k in range(4):
                    if arr[i + dx[k]][j + dy[k]] not in abc:
                        arr[i+dx[k]][j+dy[k]] = 'X'
            if arr[i][j] == 'B':
                for k in range(4):
                    for t in range(1,3):
                        if arr[i + dx[k]*t][j + dy[k]*t] not in abc:
                            arr[i+dx[k]*t][j+dy[k]*t] = 'X'
            if arr[i][j] == 'C':
                for k in range(4):
                    for t in range(1, 4):
                        if arr[i + dx[k]*t][j + dy[k]*t] not in abc:
                            arr[i+dx[k]*t][j+dy[k]*t] = 'X'

    count = 0
    for i in range(number+6):
        for j in range(number+6):
            if arr[i][j] == 'H':
                count += 1


    return count




testcase=int(input())
for i in range(1,testcase + 1):
    number = int(input())
    arr =[['X']*(number+6)]*3 + [['x']*3 + list(map(str,input())) +['X']*3 for i in range(number)] + [['X']*(number+6)]*3
    print('#{} {}'.format(i, tel()))
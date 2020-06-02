import sys
sys.stdin = open('문제2.txt', 'r')

def second():
    global row, col, numbers, change_area, empty_area

    for n in range(numbers):
        for i in range(row):
            for j in range(col):
                if i >= (change_area[n][0]-1) and i<= (change_area[n][2]-1):
                    if j >= (change_area[n][1]-1) and j<= (change_area[n][3]-1):
                        empty_area[i][j] += 1

    max_value = [0]
    for i in range(row):
        if max(empty_area[i]) > max_value[-1]:
            max_value.append(max(empty_area[i]))
    real_max = max_value[-1]

    count = 0
    for i in range(row):
        for j in range(col):
            if empty_area[i][j] == real_max:
                count+=1

    return count

testcase = int(input())
for i in range(1, testcase+1):
    options = list(map(int,input().split()))
    row = options[0]
    col = options[1]
    numbers = options[2]
    change_area = [list(map(int,input().split())) for i in range(numbers)]
    empty_area = [[0]*col for i in range(row)]
    print('#{} {}'.format(i, second()))

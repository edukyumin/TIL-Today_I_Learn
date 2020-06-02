import sys
sys.stdin = open('문제1.txt', 'r')

def first():
    global a_filter, b_filter, area
    a_basic_sum = 0
    a_change_sum = 0
    b_basic_sum = 0
    b_change_sum = 0
    for i in range(10):
        for j in range(10):
            #a필터
            if i >= a_filter[0] and i <= a_filter[2]:
                if j >= a_filter[1] and j <= a_filter[3]:
                    a_basic_sum += area[i][j]

                    area[i][j] = int(area[i][j] * 2)
                    if area[i][j] > 255:
                        area[i][j] = 255
                    a_change_sum += area[i][j]
            a_result = a_change_sum - a_basic_sum

            if i >= b_filter[0] and i <= b_filter[2]:
                if j >= b_filter[1] and j <= b_filter[3]:
                    b_basic_sum += area[i][j]

                    area[i][j] = int(area[i][j] * 0.5)
                    b_change_sum += area[i][j]

            b_result = b_basic_sum - b_change_sum


    return a_result + b_result




testcase = int(input())
for i in range(1, testcase+1):
    a_filter = list(map(int,input().split()))
    b_filter = list(map(int,input().split()))
    area = [list(map(int,input().split())) for i in range(10)]
    # print(a_filter)
    # print(b_filter)
    print('#{} {}'.format(i, first()))

import sys
sys.stdin = open('스도쿠검증_1974.txt', 'r')


def sd():
    for i in range(9):
        gob = 1
        hap = 0
        for j in range(9):
            gob *= arr[i][j]
            hap += arr[i][j]
        if hap == 45 and gob == 362880:
            continue
        else:
            return 0
    for i in range(9):
        gob = 1
        hap = 0
        for j in range(9):
            gob *= arr[j][i]
            hap += arr[j][i]
        if hap == 45 and gob == 362880:
            continue
        else:
            return 0

    for k in range(3):
        for l in range(3):
            gob = 1
            hap = 0
            for i in range(3):
                for j in range(3):
                    gob *= arr[i + 3 * k][j + 3 * l]
                    hap += arr[i + 3 * k][j + 3 * l]
            if hap == 45 and gob == 362880:
                continue
            else:
                return 0

    return 1


tc = int(input())
for i in range(1, tc + 1):
    arr = [list(map(int, input().split())) for i in range(9)]
    print('#{} {}'.format(i, sd()))
import sys
sys.stdin = open('파리퇴치_2001.txt', 'r')

def fly(m, n, area):
    fly_killed = []

    for a in range(m-n+1):
        for b in range(m-n+1):
            result = 0
            for i in range(a,a + n):
                for j in range(b, b+n):
                    result += area[i][j]
            fly_killed.append(result)
    return max(fly_killed)


testcase = int(input())
for i in range(1, testcase + 1):
    m, n = list(map(int, input().split()))
    # print(m, n)
    area = []
    for j in range(m):
        area.append(list(map(int, input().split())))
    # print(area)

    print('#{} {}'.format(i, fly(m, n, area)))
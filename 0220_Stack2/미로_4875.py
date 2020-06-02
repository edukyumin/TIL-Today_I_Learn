import sys
sys.stdin = open('미로_4875.txt', 'r')

def func():
         #서 동 남 북
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    stack = []
    visited = [[0]*number for i in range(number)]

    #시작점찾기
    for i in range(number):
        for j in range(number):
            if miro[i][j] == 2:
                stack.append([i, j])

    #이동 시작
    while len(stack) > 0:
        x, y =stack.pop(-1)
        # print(x, y)
        if visited[x][y] != 1:
            visited[x][y] = 1

            for i in range(4):
                try:
                    if x+dx[i]>=0 and y+dy[i]>=0:
                        if miro[x+dx[i]][y+dy[i]] == 0 and visited[x+dx[i]][y+dy[i]] == 0:
                            stack.append([x+dx[i], y+dy[i]])

                        elif miro[x + dx[i]][y + dy[i]] == 3:
                            return 1
                except IndexError:
                    continue
    return 0

testcase = int(input())
for i in range(1, testcase + 1):
    number = int(input())
    miro = [list(map(int, input())) for i in range(number)]

    print('#{} {}'.format(i, func()))







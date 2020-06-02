import sys
sys.stdin = open('미로1_1226.txt', 'r')

def func():
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    stack = []
    visited = [[0]*16 for i in range(16)]

    #시작점찾기
    for i in range(16):
        for j in range(16):
            if miro[i][j] == 2:
                stack.append([i, j])

    #이동 시작
    while len(stack) > 0:
        x, y =stack.pop(-1)
        if visited[x][y] != 1:
            visited[x][y] = 1

            for i in range(4):
                if miro[x+dx[i]][y+dy[i]] == 0 and visited[x+dx[i]][y+dy[i]] == 0:
                    stack.append([x+dx[i], y+dy[i]])
                elif miro[x + dx[i]][y + dy[i]] == 3:
                    return 1
    return 0

testcase = 10
for i in range(1, testcase + 1):
    number = int(input())
    miro = [list(map(int, input())) for i in range(16)]
    print('#{} {}'.format(number, func()))







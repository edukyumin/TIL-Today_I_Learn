import sys
sys.stdin = open('별자리.txt', 'r')

def star():
    dx = [1, -1, 0, 0, 1, 1, -1, -1]
    dy = [0, 0, 1, -1, 1, -1, 1, -1]
    visited = [[0]*10 for i in range(10)]
    stack = []
    cnt = 0
    for i in range(10):
        for j in range(10):
            if sky[i][j] == 1:
                if visited[i][j] == 0:
                    visited[i][j] = 1
                    stack.append([i, j])
                    while len(stack) != 0:
                        way = stack[-1]
                        visited[way[0]][way[1]] = 1
                        stack.pop(-1)
                        for k in range(8):
                            if 0 <= way[0]+dx[k] <= 9 and 0 <= way[1]+dy[k] <= 9:
                                if sky[way[0]+dx[k]][way[1]+dy[k]] == 1:
                                    if visited[way[0]+dx[k]][way[1]+dy[k]] == 0:
                                        stack.append([way[0]+dx[k], way[1]+dy[k]])
                    cnt += 1
    return cnt
testcase = int(input())
for i in range(1, testcase+1):
    sky = [list(map(int, input().split())) for j in range(10)]
    print('#{} {}'.format(i, star()))
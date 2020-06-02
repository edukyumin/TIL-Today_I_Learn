import sys
sys.stdin = open("input.txt", "r")


def is_Wall(x, y):
    if 0 <= x < N and 0 <= y < N and visited[x][y] == 0 and miro[x][y] != 1:
        return True
    return False


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    miro = [list(map(int, input())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    q = []
    result = 0
    bp = 0
    for i in range(N):
        for j in range(N):
            if miro[i][j] == 2:
                visited[i][j] = 1
                q.append([i, j])
    while q:
        x, y = q.pop(0)
        for p in range(4):
            next_x = x + dx[p]
            next_y = y + dy[p]
            if is_Wall(next_x, next_y):
                if miro[next_x][next_y] == 3:
                    result = visited[x][y] - 1
                    bp = 1
                    break
                else:
                    visited[next_x][next_y] = visited[x][y] + 1
                    q.append([next_x, next_y])
        if bp == 1:
            break

    print('#{} {}'.format(tc, result))
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())
    graph = [[0]*(V+1) for _ in range(V+1)]
    for i in range(E):
        graph[data[i][0]][data[i][1]] = 1
        graph[data[i][1]][data[i][0]] = 1
    q = []
    q.append(S)
    visited = [0]*(V+1)
    visited[S] = 1
    t = 0
    result = 0
    d = 0
    while q:
        t = q.pop(0)
        d += 1
        for u in range(1, V+1):
            if graph[t][u] == 1 and visited[u] == 0:
                q.append(u)
                visited[u] = visited[t] + 1
                if u == G:
                    result = visited[u] - 1
                    break
    print('#{} {}'.format(tc, result))
import sys
sys.stdin = open('DFS.txt', 'r')
def DFS(s):
    stack = []
    visited = [0, 0, 0, 0, 0, 0, 0, 0]
    graph = [[0]* 8 for i in range(8)]
    way = []
    for i in range(r):
        graph[lines[i][0]][lines[i][1]] = 1
        graph[lines[i][1]][lines[i][0]] = 1

    stack.append(s)
    while len(stack) > 0:
        print(stack)
        where = stack.pop(-1)
        print('{}을 pop함'.format(where))
        if visited[where] != 1:
            visited[where] = 1
            print('간적없으므로 {}로 가겟음'.format(where))
            way.append(where)

            for w in range(8):
                if graph[where][w] == 1 and visited[w] != 1:
                    stack.append(w)
                    print('{}는 간적도 없고 갈수잇다'.format(w))
    return way

n, r = list(map(int,input().split()))
lines = []
for i in range(r):
    lines.append(list(map(int, input().split())))
print(lines)
print(DFS(1))

#--------------------------



# import sys
# sys.stdin = open('DFS.txt', 'r')
# V = [1, 2, 3, 4, 5, 6, 7]
# lines= []
# graph = [[0]*(len(V)+1) for i in range(len(V)+1)]
#
# stack = []
# visited = [0] * (len(V)+1)
# result = []
# def DFS(v):
#     for i in range(len(V)+1):
#         graph[lines[i][0]][lines[i][1]] = 1
#         graph[lines[i][1]][lines[i][0]] = 1
#     print(graph)
#     stack.append(v)
#     while len(stack) > 0:
#         v = stack.pop(-1)
#         if visited[v] != 1:
#             visited[v] = 1
#             result.append(v)
#
#             for w in range(1,len(V)+1):
#                 if graph[v][w] == 1 and visited[w] ==0:
#                     stack.append(w)
#     return result
#
# n, r = list(map(int, input().split()))
# for i in range(r):
#     lines.append(list(map(int, input().split())))
#
# print(lines)
# print(DFS(1))

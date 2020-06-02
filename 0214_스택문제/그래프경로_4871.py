import sys
sys.stdin = open('그래프경로_4871.txt', 'r')

def DFS():
    global v, e, arr, s, g
    graph = [[0 for i in range(v+1)] for j in range(v+1)]
    visited = [0]*(v+1)
    stack = [s]
    for i in range(e):
        graph[arr[i][0]][arr[i][1]] = 1

    while len(stack) > 0:
        start = stack.pop(-1)
        if visited[start] != 1:
            visited[start] = 1

            for w in range(1, v+1):
                if graph[start][w] == 1 and visited[w] == 0:
                    stack.append(w)
                    if w ==g:
                        return 1
    return 0

testcase = int(input())
for i in range(1, testcase + 1):
    v, e = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for i in range(e)]
    s, g = list(map(int, input().split()))
    print('#{} {}'.format(i, DFS()))


## 기문이형 재귀함수 코드
# # for로 푼것
# def ban(list_test):
#     for i in range(len(list_test)-1):
#         if list_test[i] == list_test[i+1]:
#             list_test.pop(i)
#             list_test.pop(i)
#             return ban(list_test)
#     return len(list_test)
# # while로 푼것
# def ban(list_test):
#     if len(list_test) < 2:
#         res = len(list_test)
#         return len(list_test)
#     else:
#         n = 0
#         while list_test[n] != list_test[n+1] and n < (len(list_test)-2): n += 1
#         if list_test[n] == list_test[n+1]:
#             list_test.pop(n)
#             list_test.pop(n)
#             return ban(list_test)
#         return len(list_test)
# tc = int(input())
# for testcase in range(1, tc+1):
#     list_test = list(input())
#     print('#{} {}' .format(testcase, ban(list_test)))
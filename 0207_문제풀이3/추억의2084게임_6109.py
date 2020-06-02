import sys
sys.stdin = open('추억의2084게임_6109.txt', 'r')

def game():
    global n, dir, tile
    # print(tile)
# ------------------------------------------------up, down의 경우 전치
#     if dir == 'up':
#         tile = list(map(list, zip(*tile)))
#         dir = 'left'
#     elif dir == 'down':
#         tile = list(map(list, zip(*tile)))
#         dir = 'right'
# #------------------------------------------------
#     ##왼쪽인경우 오른쪽인 경우 나누기
#     if dir == 'left':
#         range_list = range()
#


    # for i in range(n):
    #     for j in range(n+1):
    #         while tile[i][j] != 1025:







    return tile

testcase = int(input())
for i in range(1, testcase+1):
    n, dir = list(map(str, input().split()))
    n = int(n)
    if dir == 'up':
        tile = [[[1025] * n + list(map(int, input().split())) for j in range(n)]]
    elif dir == 'down':
        tile = [list(map(int, input().split())) for j in range(n)] + [[1025]*n]
    elif dir == 'left':
        tile = [[[1025] + list(map(int, input().split()))] for j in range(n)]
    elif dir == 'right':
        tile = [list(map(int, input().split())) + [1025] for j in range(n)]
    print('#{}\n{}'.format(i, game()))

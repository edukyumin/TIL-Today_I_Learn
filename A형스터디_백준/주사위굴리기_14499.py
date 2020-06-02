import sys
sys.stdin = open('주사위굴리기_14499.txt', 'r')

def dicefunc():
    global x, y
    result = []
    dice = [[0] * 5 for i in range(6)]
            #동 서  북  남
    dx = [0, 0, 0, -1, 1]
    dy = [0, 1, -1, 0, 0]
    for n in range(len(move)): #명령횟수만큼 실행
        #지도의 좌표 이동
        x += dx[move[n]]
        y += dy[move[n]]
        if 0 <= x <= N-1 and 0 <= y <= M-1:
            '''
            1. DICE 회전 : 자리를 고정하고 회전(동,서,남,북)에 따라 숫자만 바꿔준다.
            '''
            if move[n] == 1: #동
                dice[2][1] ,dice[2][2] ,dice[2][3], dice[4][2] = dice[4][2] ,dice[2][1] ,dice[2][2], dice[2][3]
            elif move[n] == 2: #서
                dice[2][1], dice[2][2], dice[2][3], dice[4][2] = dice[2][2], dice[2][3], dice[4][2], dice[2][1]
            elif move[n] == 3: #북
                dice[1][2], dice[2][2], dice[3][2], dice[4][2] = dice[2][2], dice[3][2], dice[4][2], dice[1][2]
            elif move[n] == 4: #남
                dice[1][2], dice[2][2], dice[3][2], dice[4][2] = dice[4][2], dice[1][2], dice[2][2], dice[3][2]

            '''
            2. 복사 : DICE 와 MAP 사이의 밑면만 바꾼다.
            '''
            if maps[x][y] == 0:
                maps[x][y] = dice[4][2]
            else:
                dice[4][2] = maps[x][y]
                maps[x][y] = 0

            # dice[2][2]는 항상 윗면을 가르키므로 그곳을 출력!
            result.append(str(dice[2][2]))

        else:
            x -= dx[move[n]]
            y -= dy[move[n]]

    return '\n'.join(result)
N, M, x, y, k = list(map(int, input().split()))
maps = [list(map(int, input().split())) for i in range(N)]
move = list(map(int, input().split()))
print(dicefunc())


#아래는 TRY EXCEPT 쓴 구문
# import sys
# sys.stdin = open('주사위굴리기_14499.txt', 'r')
#
# def dicefunc():
#     global x, y
#     result = []
#     dice = [[0] * 5 for i in range(6)]
#             #동 서  북  남
#     dx = [0, 0, 0, -1, 1]
#     dy = [0, 1, -1, 0, 0]
#     for n in range(len(move)): #명령횟수만큼 실행
#         #지도의 좌표 이동
#         x += dx[move[n]]
#         y += dy[move[n]]
#
#         if 0 <= x and 0 <= y:
#             try:
#                 '''
#                 1. DICE 회전 : 자리를 고정하고 회전(동,서,남,북)에 따라 숫자만 바꿔준다.
#                 '''
#                 if move[n] == 1: #동
#                     dice[2][1] ,dice[2][2] ,dice[2][3], dice[4][2] = dice[4][2] ,dice[2][1] ,dice[2][2], dice[2][3]
#                 elif move[n] == 2: #서
#                     dice[2][1], dice[2][2], dice[2][3], dice[4][2] = dice[2][2], dice[2][3], dice[4][2], dice[2][1]
#                 elif move[n] == 3: #북
#                     dice[1][2], dice[2][2], dice[3][2], dice[4][2] = dice[2][2], dice[3][2], dice[4][2], dice[1][2]
#                 elif move[n] == 4: #남
#                     dice[1][2], dice[2][2], dice[3][2], dice[4][2] = dice[4][2], dice[1][2], dice[2][2], dice[3][2]
#
#                 '''
#                 2. 복사 : DICE 와 MAP 사이의 밑면만 바꾼다.
#                 '''
#                 if maps[x][y] == 0:
#                     maps[x][y] = dice[4][2]
#                 else:
#                     dice[4][2] = maps[x][y]
#                     maps[x][y] = 0
#
#                 # dice[2][2]는 항상 윗면을 가르키므로 그곳을 출력!
#                 result.append(str(dice[2][2]))
#
#             except IndexError:
#                 x -= dx[move[n]]
#                 y -= dy[move[n]]
#
#     return '\n'.join(result)
# N, M, x, y, k = list(map(int, input().split()))
# maps = [list(map(int, input().split())) for i in range(N)]
# move = list(map(int, input().split()))
# print(dicefunc())
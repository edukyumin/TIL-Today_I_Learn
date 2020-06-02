ary = [[9, 20, 2, 18, 11], [19, 1, 25, 3, 21], [8, 24, 10, 17, 7], [15, 4, 16, 5, 6], [12, 13, 22, 23, 14]]

sorted_ary =[[0 for _ in range(5)] for _ in range(5)]
def isWall(x, y):
    if x < 0 or x >= 5 : return True # 벽에 닿거나
    if y < 0 or y >= 5 : return True
    if sorted_ary[x][y] != 0: return True # 0이 아닌 값이 이미 들어있거나 => 이경우도 어짜피 못나아가니까
                                          # 벽으로 취급
    return False
def sel_min():
    minX, minY = 0, 0
    for i in range(5):
        for j in range(5):
            if ary[minX][minY] > ary[i][j]: # (0,0) 부터 시작해서 작은 수를
                minX,minY = i,j #minX, minY 에 인덱스 저장
    min = ary[minX][minY] #작은 수의 인덱스를 이용해서 min에 저장
    ary[minX][minY] = 99 #아주 큰값으로 바꿔서 다음에 카운팅 하지 않도록 함
    return min # 작은값 호출!
ary = [[9, 20, 2, 18, 11], [19, 1, 25, 3, 21], [8, 24, 10, 17, 7], [15, 4, 16, 5, 6], [12, 13, 22, 23, 14]]
sorted_ary = [[0 for _ in range(5)]for _ in range(5)]
X, Y = 0, 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
dir_stat = 0 # 0:오른쪽, 1:아래, 2:왼쪽, 3:위
for i in range(25):
    cur_min = sel_min() # 제일 작은 값
    sorted_ary[X][Y] = cur_min #(0, 0)부터 시작해서 제일 작은 값 들어감
    X += dx[dir_stat]
    Y += dy[dir_stat] # dx, dy 이용해서 이동함
    if isWall(X, Y): # 만약에 벽에 닿게 되면
        X -= dx[dir_stat]
        Y -= dy[dir_stat] # 다시 전 위치로 돌아감
        dir_stat = (dir_stat + 1) % 4 # dx, dy 배열을 돌릴때 마지막 요소에서 다시 처음 요소로 돌아가야 하니까
        X = X + dx[dir_stat]          # 4로 나눈 나머지를 이용해서 계속 돌린다.
        Y = Y + dy[dir_stat]
for i in range(5):
    for j in range(5):
        print(sorted_ary[i][j], end=' ')
    print()
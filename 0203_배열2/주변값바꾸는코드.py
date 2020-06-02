my_array = [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]]
#자기주변숫자와의 차이를 구하는 함수

##선생님 코드
def isWall(x,y):
    if x < 0 or x >= 5: return True
    if y < 0 or y >= 5: return True
    return False
dx = [0, 0,-1, 1]
dy = [-1,1,0,0]
sum = 0
for x in range(len(my_array)):
    for y in range(len(my_array[0])):
        for i in range(4):
            testX = x + dx[i]
            testY = y + dy[i]
            if isWall(testX, testY) == False:
                sum += abs(my_array[x][y] - my_array[testX][testY])

print(sum)

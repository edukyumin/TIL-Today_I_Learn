import sys
sys.stdin = open('미세먼지안녕_백준_17144.txt', 'r')

def PM():
    for k in range(t):
        sum_arr = [[0]*c for i in range(r)]
        #확산코드
        for i in range(r):
            for j in range(c):
                dx = [1, -1, 0, 0]
                dy = [0, 0, 1, -1]

                if arr[i][j] != -1 and arr[i][j] != 0:
                    gab = arr[i][j]
                    sum_count = 0
                    for d in range(4):
                        if 0 <= i+dx[d] <= r-1 and 0 <= j+dy[d] <= c-1 and arr[i+dx[d]][j+dy[d]] != -1:
                            sum_arr[i+dx[d]][j+dy[d]] += gab // 5
                            sum_count += 1

                    arr[i][j] -= (arr[i][j]//5) * sum_count
                    # print('i,j는 {},{}'.format(i,j))
                    # print(arr)
        for i in range(r):
            for j in range(c):
                arr[i][j] += sum_arr[i][j]

        #공기청정
        air = []
        for i in range(r):
            for j in range(c):
                if arr[i][j] == -1:
                    air.append(i)
        empty_arr = [[0]*c for i in range(r)]
        for i in range(r):
            for j in range(c):
                if j == 0 and 1 <= i <= air[0]:
                    empty_arr[i][j] = arr[i-1][j]
                elif j == 0 and air[1]<= i <= r-2:
                    empty_arr[i][j] = arr[i+1][j]


                elif i == air[0] and 1 <= j <= c-1:
                    empty_arr[i][j] = arr[i][j-1]
                elif i == air[1] and 1 <= j <= c-1:
                    empty_arr[i][j] = arr[i][j-1]

                elif j == c-1 and 0 <= i <= air[0]-1:
                    empty_arr[i][j] = arr[i+1][j]
                elif j == c-1 and air[1]+1 <= i <= r-1:
                    empty_arr[i][j] = arr[i-1][j]
                elif i == 0 and 0 <= j <= c-2:
                    empty_arr[i][j] = arr[i][j+1]
                elif i == r-1 and 0<= j <= c-2:
                    empty_arr[i][j] = arr[i][j+1]

                else:
                    empty_arr[i][j] = arr[i][j]

                if empty_arr[i][j] == -1:
                    empty_arr[i][j] = 0

                empty_arr[air[0]][0] = -1
                empty_arr[air[1]][0] = -1


    result = 0
    for i in range(r):
        for j in range(c):
            result += empty_arr[i][j]

    return result



r, c, t = list(map(int,input().split()))
arr = [list(map(int,input().split())) for i in range(r)]
print(PM())
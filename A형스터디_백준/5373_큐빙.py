import sys
sys.stdin = open('5373_큐빙.txt', 'r')

def cubing():
    cube = [['*', '*', '*', 'o', 'o', 'o', '*', '*', '*'],
            ['*', '*', '*', 'o', 'o', 'o', '*', '*', '*'],
            ['*', '*', '*', 'o', 'o', 'o', '*', '*', '*'],
            ['g', 'g', 'g', 'w', 'w', 'w', 'b', 'b', 'b'],
            ['g', 'g', 'g', 'w', 'w', 'w', 'b', 'b', 'b'],
            ['g', 'g', 'g', 'w', 'w', 'w', 'b', 'b', 'b'],
            ['*', '*', '*', 'r', 'r', 'r', '*', '*', '*'],
            ['*', '*', '*', 'r', 'r', 'r', '*', '*', '*'],
            ['*', '*', '*', 'r', 'r', 'r', '*', '*', '*'],
            ['*', '*', '*', 'y', 'y', 'y', '*', '*', '*'],
            ['*', '*', '*', 'y', 'y', 'y', '*', '*', '*'],
            ['*', '*', '*', 'y', 'y', 'y', '*', '*', '*'],
            ]

    for i in range(number):
        if arr[i] == 'U+':
            save = [cube[6][3], cube[6][4], cube[6][5]]
            cube[6][3], cube[6][4], cube[6][5] = cube[5][6], cube[4][6], cube[3][6]
            cube[5][6], cube[4][6], cube[3][6] = cube[2][5], cube[2][4], cube[2][3]
            cube[2][5], cube[2][4], cube[2][3] = cube[3][2], cube[4][2], cube[5][2]
            cube[3][2], cube[4][2], cube[5][2] = save[0], save[1], save[2]

            self = [cube[5][3], cube[5][4], cube[5][5]]
            cube[5][3], cube[5][4], cube[5][5] = cube[5][5], cube[4][5], cube[3][5]
            cube[5][5], cube[4][5], cube[3][5] = cube[3][5], cube[3][4], cube[3][3]
            cube[3][5], cube[3][4], cube[3][3] = cube[3][3], cube[4][3], cube[5][3]
            cube[3][3], cube[4][3], cube[5][3] = self[0], self[1], self[2]
        elif arr[i] == 'U-':
            save = [cube[6][3], cube[6][4], cube[6][5]]
            cube[6][3], cube[6][4], cube[6][5] = cube[3][2], cube[4][2], cube[5][2]
            cube[3][2], cube[4][2], cube[5][2] = cube[2][5], cube[2][4], cube[2][3]
            cube[2][5], cube[2][4], cube[2][3] = cube[5][6], cube[4][6], cube[3][6]
            cube[5][6], cube[4][6], cube[3][6] = save[0], save[1], save[2]

            self = [cube[5][3], cube[5][4], cube[5][5]]
            cube[5][3], cube[5][4], cube[5][5] = cube[3][3], cube[4][3], cube[5][3]
            cube[3][3], cube[4][3], cube[5][3] = cube[3][5], cube[3][4], cube[3][3]
            cube[3][5], cube[3][4], cube[3][3] = cube[5][5], cube[4][5], cube[3][5]
            cube[5][5], cube[4][5], cube[3][5] = self[0], self[1], self[2]
        elif arr[i] == 'D+':
            save = [cube[0][3], cube[0][4], cube[0][5]]
            cube[0][3], cube[0][4], cube[0][5] = cube[3][8], cube[4][8], cube[5][8]
            cube[3][8], cube[4][8], cube[5][8] = cube[8][5], cube[8][4], cube[8][3]
            cube[8][5], cube[8][4], cube[8][3] = cube[5][0], cube[4][0], cube[3][0]
            cube[5][0], cube[4][0], cube[3][0] = save[0], save[1], save[2]

            self = [cube[11][3], cube[11][4], cube[11][5]]
            cube[11][3], cube[11][4], cube[11][5] = cube[11][5], cube[10][5], cube[9][5]
            cube[11][5], cube[10][5], cube[9][5] = cube[9][5], cube[9][4], cube[9][3]
            cube[9][5], cube[9][4], cube[9][3] = cube[9][3], cube[10][3], cube[11][3]
            cube[9][3], cube[10][3], cube[11][3] = self[0], self[1], self[2]
        elif arr[i] == 'D-':
            save = [cube[0][3], cube[0][4], cube[0][5]]
            cube[0][3], cube[0][4], cube[0][5] = cube[5][0], cube[4][0], cube[3][0]
            cube[5][0], cube[4][0], cube[3][0] = cube[8][5], cube[8][4], cube[8][3]
            cube[8][5], cube[8][4], cube[8][3] = cube[3][8], cube[4][8], cube[5][8]
            cube[3][8], cube[4][8], cube[5][8] = save[0], save[1], save[2]

            self = [cube[11][3], cube[11][4], cube[11][5]]
            cube[11][3], cube[11][4], cube[11][5] = cube[9][3], cube[10][3], cube[11][3]
            cube[9][3], cube[10][3], cube[11][3] = cube[9][5], cube[9][4], cube[9][3]
            cube[9][5], cube[9][4], cube[9][3] = cube[11][5], cube[10][5], cube[9][5]
            cube[11][5], cube[10][5], cube[9][5] = self[0], self[1], self[2]
        elif arr[i] == 'F+':
            save = [cube[9][3], cube[9][4], cube[9][5]]
            cube[9][3], cube[9][4], cube[9][5] = cube[5][8], cube[5][7], cube[5][6]
            cube[5][8], cube[5][7], cube[5][6] = cube[5][5], cube[5][4], cube[5][3]
            cube[5][5], cube[5][4], cube[5][3] = cube[5][2], cube[5][1], cube[5][0]
            cube[5][2], cube[5][1], cube[5][0] = save[0], save[1], save[2]

            self = [cube[8][3], cube[8][4], cube[8][5]]
            cube[8][3], cube[8][4], cube[8][5] = cube[8][5], cube[7][5], cube[6][5]
            cube[8][5], cube[7][5], cube[6][5] = cube[6][5], cube[6][4], cube[6][3]
            cube[6][5], cube[6][4], cube[6][3] = cube[6][3], cube[7][3], cube[8][3]
            cube[6][3], cube[7][3], cube[8][3] = self[0], self[1], self[2]
        elif arr[i] == 'F-':
            save = [cube[9][3], cube[9][4], cube[9][5]]
            cube[9][3], cube[9][4], cube[9][5] = cube[5][2], cube[5][1], cube[5][0]
            cube[5][2], cube[5][1], cube[5][0] = cube[5][5], cube[5][4], cube[5][3]
            cube[5][5], cube[5][4], cube[5][3] = cube[5][8], cube[5][7], cube[5][6]
            cube[5][8], cube[5][7], cube[5][6] = save[0], save[1], save[2]

            self = [cube[8][3], cube[8][4], cube[8][5]]
            cube[8][3], cube[8][4], cube[8][5] = cube[6][3], cube[7][3], cube[8][3]
            cube[6][3], cube[7][3], cube[8][3] = cube[6][5], cube[6][4], cube[6][3]
            cube[6][5], cube[6][4], cube[6][3] = cube[8][5], cube[7][5], cube[6][5]
            cube[8][5], cube[7][5], cube[6][5] = self[0], self[1], self[2]
        elif arr[i] == 'B+':
            save = [cube[3][3], cube[3][4], cube[3][5]]
            cube[3][3], cube[3][4], cube[3][5] = cube[3][6], cube[3][7], cube[3][8]
            cube[3][6], cube[3][7], cube[3][8] = cube[11][5], cube[11][4], cube[11][3]
            cube[11][5], cube[11][4], cube[11][3] = cube[3][0], cube[3][1], cube[3][2]
            cube[3][0], cube[3][1], cube[3][2] = save[0], save[1], save[2]

            self = [cube[2][3], cube[2][4], cube[2][5]]
            cube[2][3], cube[2][4], cube[2][5] = cube[2][5], cube[1][5], cube[0][5]
            cube[2][5], cube[1][5], cube[0][5] = cube[0][5], cube[0][4], cube[0][3]
            cube[0][5], cube[0][4], cube[0][3] = cube[0][3], cube[1][3], cube[2][3]
            cube[0][3], cube[1][3], cube[2][3] = self[0], self[1], self[2]
        elif arr[i] == 'B-':
            save = [cube[3][3], cube[3][4], cube[3][5]]
            cube[3][3], cube[3][4], cube[3][5] = cube[3][0], cube[3][1], cube[3][2]
            cube[3][0], cube[3][1], cube[3][2] = cube[11][5], cube[11][4], cube[11][3]
            cube[11][5], cube[11][4], cube[11][3] = cube[3][6], cube[3][7], cube[3][8]
            cube[3][6], cube[3][7], cube[3][8] = save[0], save[1], save[2]

            self = [cube[2][3], cube[2][4], cube[2][5]]
            cube[2][3], cube[2][4], cube[2][5] = cube[0][3], cube[1][3], cube[2][3]
            cube[0][3], cube[1][3], cube[2][3] = cube[0][5], cube[0][4], cube[0][3]
            cube[0][5], cube[0][4], cube[0][3] = cube[2][5], cube[1][5], cube[0][5]
            cube[2][5], cube[1][5], cube[0][5] = self[0], self[1], self[2]
        elif arr[i] == 'L+':
            save = [cube[8][3], cube[7][3], cube[6][3]]
            cube[8][3], cube[7][3], cube[6][3] = cube[5][3], cube[4][3], cube[3][3]
            cube[5][3], cube[4][3], cube[3][3] = cube[2][3], cube[1][3], cube[0][3]
            cube[2][3], cube[1][3], cube[0][3] = cube[11][3], cube[10][3], cube[9][3]
            cube[11][3], cube[10][3], cube[9][3] = save[0], save[1], save[2]

            self = [cube[5][0], cube[5][1], cube[5][2]]
            cube[5][0], cube[5][1], cube[5][2] = cube[5][2], cube[4][2], cube[3][2]
            cube[5][2], cube[4][2], cube[3][2] = cube[3][2], cube[3][1], cube[3][0]
            cube[3][2], cube[3][1], cube[3][0] = cube[3][0], cube[4][0], cube[5][0]
            cube[3][0], cube[4][0], cube[5][0] = self[0], self[1], self[2]
        elif arr[i] == 'L-':
            save = [cube[8][3], cube[7][3], cube[6][3]]
            cube[8][3], cube[7][3], cube[6][3] = cube[11][3], cube[10][3], cube[9][3]
            cube[11][3], cube[10][3], cube[9][3] = cube[2][3], cube[1][3], cube[0][3]
            cube[2][3], cube[1][3], cube[0][3] = cube[5][3], cube[4][3], cube[3][3]
            cube[5][3], cube[4][3], cube[3][3] = save[0], save[1], save[2]

            self = [cube[5][0], cube[5][1], cube[5][2]]
            cube[5][0], cube[5][1], cube[5][2] = cube[3][0], cube[4][0], cube[5][0]
            cube[3][0], cube[4][0], cube[5][0] = cube[3][2], cube[3][1], cube[3][0]
            cube[3][2], cube[3][1], cube[3][0] = cube[5][2], cube[4][2], cube[3][2]
            cube[5][2], cube[4][2], cube[3][2] = self[0], self[1], self[2]
        elif arr[i] == 'R+':
            save = [cube[6][5], cube[7][5], cube[8][5]]
            cube[6][5], cube[7][5], cube[8][5] = cube[9][5], cube[10][5], cube[11][5]
            cube[9][5], cube[10][5], cube[11][5] = cube[0][5], cube[1][5], cube[2][5]
            cube[0][5], cube[1][5], cube[2][5] = cube[3][5], cube[4][5], cube[5][5]
            cube[3][5], cube[4][5], cube[5][5] = save[0], save[1], save[2]

            self = [cube[5][6], cube[5][7], cube[5][8]]
            cube[5][6], cube[5][7], cube[5][8] = cube[5][8], cube[4][8], cube[3][8]
            cube[5][8], cube[4][8], cube[3][8] = cube[3][8], cube[3][7], cube[3][6]
            cube[3][8], cube[3][7], cube[3][6] = cube[3][6], cube[4][6], cube[5][6]
            cube[3][6], cube[4][6], cube[5][6] = self[0], self[1], self[2]
        elif arr[i] == 'R-':
            save = [cube[6][5], cube[7][5], cube[8][5]]
            cube[6][5], cube[7][5], cube[8][5] = cube[3][5], cube[4][5], cube[5][5]
            cube[3][5], cube[4][5], cube[5][5] = cube[0][5], cube[1][5], cube[2][5]
            cube[0][5], cube[1][5], cube[2][5] = cube[9][5], cube[10][5], cube[11][5]
            cube[9][5], cube[10][5], cube[11][5] = save[0], save[1], save[2]

            self = [cube[5][6], cube[5][7], cube[5][8]]
            cube[5][6], cube[5][7], cube[5][8] = cube[3][6], cube[4][6], cube[5][6]
            cube[3][6], cube[4][6], cube[5][6] = cube[3][8], cube[3][7], cube[3][6]
            cube[3][8], cube[3][7], cube[3][6] = cube[5][8], cube[4][8], cube[3][8]
            cube[5][8], cube[4][8], cube[3][8] = self[0], self[1], self[2]

    result = '{}{}{}\n{}{}{}\n{}{}{}'.format(cube[3][3], cube[3][4], cube[3][5], cube[4][3], cube[4][4], cube[4][5], cube[5][3], cube[5][4], cube[5][5])

    return result

testcase = int(input())
for i in range(testcase):
    number = int(input())
    arr = list(map(str, input().split()))
    print(cubing())
import sys
import copy
sys.stdin = open('Ladder2_1211.txt', 'r')

def Ladder(problems):
    distance = [0 for i in range(102)]
    start_idx = []
    first_line = problems[0]
    for i in range(102):
        if first_line[i] == 1:
            start_idx.append(i)
    for j in start_idx:
        fake = copy.deepcopy(problems)
        count = 0
        a = j
        i = 0


            while i <= 99:
            if fake[i][j + 1] != 1 and fake[i][j - 1] != 1:
                fake[i][j] = 0
                i += 1
                count += 1
            elif fake[i][j + 1] == 1:
                fake[i][j] = 0
                j += 1
                count += 1

            elif fake[i][j - 1] == 1:
                fake[i][j] = 0
                j -= 1
                count += 1

        distance[a] = count

    for z in range(102):
        if distance[z] == 0:
            distance[z] = 9999
    return distance.index(min(distance))-1

testcase = 10
for i in range(1, testcase + 1):
    problems = []
    number = int(input())
    for j in range(100):
        problem = list(map(int, input().split()))
        problems.append([0] + problem + [0])
    print('#{} {}'.format(number, Ladder(problems)))

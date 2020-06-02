import sys
sys.stdin = open('어디에단어가_1979.txt','r')

def where():
    global puzzle
    count = 0
    # 행 연산
    for i in range(len(puzzle)):
        for j in range(len(puzzle[0]) - k + 1):
            if sum(puzzle[i][j:j+k]) == k:
                if sum(puzzle[i][j:j + k + 1]) != k+1:
                    if j >=1:
                        if sum(puzzle[i][j-1:j + k ]) != k + 1:
                            count += 1

                    else:
                        count += 1


    puzzle = list(map(list, zip(*puzzle)))

    # 열 연산
    for i in range(len(puzzle)):
        for j in range(len(puzzle[0]) - k + 1):
            if sum(puzzle[i][j:j+k]) == k:
                if sum(puzzle[i][j:j + k + 1]) != k+1:
                    if j >=1:
                        if sum(puzzle[i][j-1:j + k ]) != k + 1:
                            count += 1
                    else:
                        count += 1


    return count
testcase = int(input())
for i in range(1, testcase + 1):
    n, k = list(map(int, input().split()))
    puzzle = [list(map(int, input().split())) for i in range(n)]
    print('#{} {}'.format(i, where()))
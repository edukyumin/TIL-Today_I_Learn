import sys
sys.stdin = open('회문1_1215.txt', 'r')
def hwe():
    count = 0
    for i in range (8):
        for j in range(8 - length + 1):
            if letters[i][j:j+length] == letters[i][j:j+length][::-1]:
                count += 1
            selo = ''
            for k in range(length):
                selo += letters[j+k][i]
            if selo == selo[::-1]:
                count+=1
    return count
testcase = 10
for i in range(1, testcase + 1):
    length = int(input())
    letters = [input() for i in range(8)]
    # print(letters)
    print('#{} {}'.format(i, hwe()))
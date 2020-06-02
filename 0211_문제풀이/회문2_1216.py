import sys
sys.stdin = open('회문2_1216.txt', 'r')
def hwe():
    result = ['']
    for length in range(0, 100):
        for i in range(100):
            selo = ''
            for j in range(100 - length):

                if letters[i][j:j+length+1] == letters[i][j:j+length+1][::-1]:
                    if len(letters[i][j:j+length+1]) > len(result[-1]):
                        result[0] = letters[i][j:j+length+1]
                selo += letters[j + length ][i]
                if selo == selo[::-1]:
                    if len(selo) > len(result[0]):
                        result[0] = selo
    return len(result[0])
testcase = 10
for i in range(1, testcase + 1):
    number = int(input())
    letters = [input() for i in range(100)]
    print('#{} {}'.format(number, hwe()))
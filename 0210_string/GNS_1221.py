import sys
sys.stdin = open('GNS_1221.txt', 'r')

def GNS():
    global number, length, letters
    my_list = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    for i in range(length):
        letters[i] = my_list.index(letters[i])
    letters.sort()
    for j in range(length):
        letters[j] = my_list[letters[j]]

    result = ' '.join(letters)
    return result


testcase = int(input())
for i in range(1, testcase+1):
    number, length = list(map(str,input().split()))
    length = int(length)
    letters = list(map(str,input().split()))
    # print(letters)
    print('#{}\n{}'.format(i, GNS()))
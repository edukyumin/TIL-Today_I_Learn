import sys
sys.stdin = open('농작물수확하기_2805.txt', 'r')
def nong():
    # global length, arr
    result = 0
    for i, j in zip(range(length), range(length//2, -(length//2)-1, -1)):
        j = abs(j)
        if j ==0:
            result += sum(arr[i])
        else:
            result += sum(arr[i][j:-j])
    return result
testcase = int(input())
for i in range(1, testcase+1):
    length = int(input())
    arr = [list(map(int,input())) for i in range(length)]
    print('#{} {}'.format(i, nong()))



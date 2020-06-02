import sys
sys.stdin = open('숫자배열회전_1961.txt', 'r')

def hw():
    results = ''
    for i in range(len):
        first, second, third = '', '', ''
        for j in range(len):
            first += arr[len-j-1][i]
            second += arr[-i-1][-j-1]
            third += arr[j][len-i-1]
        result = first + ' ' + second + ' '+ third
        if i != len-1:
            results+= result +'\n'
        else:
            results+= result
    return results
tc = int(input())
for i in range(1, tc + 1):
    len = int(input())
    arr = [list(map(str, input().split())) for i in range(len)]
    print('#{}\n{}'.format(i, hw()))
import sys
sys.stdin = open('문자열비교_4864.txt', 'r')
def func():
    global first, second
    for x in range(0, len(second)-len(first)+1):
        for j, i in zip(range(x, len(first) +x), range(len(first))):
            if second[j:j+len(first)] == first:
                return 1
    return 0
testcase = int(input())
for i in range(1, testcase+1):
    first = input()
    second = input()
    print('#{} {}'.format(i, func()))
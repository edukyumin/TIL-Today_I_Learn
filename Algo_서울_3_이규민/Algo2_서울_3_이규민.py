import sys
sys.stdin=open('Algo2_서울_3_이규민.txt', 'r')

def func():
    result = ''
    return result

testcase = int(input())
for i in range(1,testcase):
    N=int(input())
    arr= [list(map(int,input().split())) for i in range(N)]
    print('#{} {}'.format(i,func()))
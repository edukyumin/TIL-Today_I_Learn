import sys
sys.stdin = open('피자굽기_5099.txt', 'r')

def func():
    q= pizza[0:M]
    result = []
    while len(q) !=0:
        first = q.pop(0)
        first[0] = first[0]//2
        if first[0] == 0:
            result.append(first)
            q.append()
        else:
            q.append(first)


    return q

testcase = int(input())
for i in range(1, testcase+1):
    M, C = list(map(int, input().split()))
    piz = list(map(int, input().split()))
    pizza=[]
    for j in range(C):
        pizza.append([piz[j], j+1])
    print('#{} {}'.format(i, func()))
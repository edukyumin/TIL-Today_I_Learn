import sys
sys.stdin = open('metal_1259.txt', 'r')

def metal():
    global number, arr
    su = []
    am = []
    result = []
    for i in range(2*number):
        if i % 2 == 0:
            su.append(arr[i])
        else:
            am.append(arr[i])
    for i in range(len(su)):
        if su[i] not in am:
            start = su[i]
            break
    result.append(start)
    result.append(am[su.index(start)])
    for i in range(number-1):
        if result[-1] in su:
            result.append(su[su.index(result[-1])])
        result.append(am[su.index(result[-1])])
    return ' '.join(map(str,result))
testcase = int(input())

for i in range(1, 1+testcase):
    number = int(input())
    arr = list(map(int, input().split()))
    print('#{} {}'.format(i, metal()))
































#두가지 방법으로 풀어보기
#1. 한개한개 제일 앞에 넣어보면서 길이가 가장 길에 연결할 수 있는 경우
#2. 홀수, 짝수번째를 따로 넣어서 .index() 함수 이용하여 푸는법
## 제일 첫 막대를 먼저 선정 (암or수가 없이 혼자만잇는애) 그 후에 한개씩 조합
#3. insert와  append함수 이용해서
## 첫번째껄 기준으로 뒤에붙으면 append 앞에붙으면 insert로 붙이기


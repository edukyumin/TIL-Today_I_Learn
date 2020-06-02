import sys
sys.stdin= open('정곤이의단조증가수_6190.txt', 'r')

testcase = int(input())

for i in range(1, testcase+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    result = []
    for x in range(len(numbers)):
        for y in range(x+1, N):
            z = numbers[x] * numbers[y]
            strZ =str(z)

            count = 0
            for l in range(len(strZ)-1):
                if strZ[l] <= strZ[l+1]:
                    count += 1
                else:
                    break
            if count == len(strZ)-1:   #만약 COUNT가 문자열길이 -1 만큼 돈 경우 즉, 단조증가수인경우
                result.append(z)
    print(result)


    if len(result) > 0:
        final = max(result)
    else:
        final = -1
    print('#{} {}'.format(i, final))



import sys

sys.stdin = open('building_input.txt', 'r')  #file에서 읽어온값을 키보드에서 입력한것으로 간주하겠다는것 r은 읽기전용이라는것

# sys.stdout = open('1206input.txt', 'w') ##결과를 파일에 write한다

testcase = 10
# testcase = int(input())

for i in range(1, testcase+1):
    n = int(input())
    result = 0
    buildings = list(map(int, input().split()))    #빌딩의 높이
    for j in range(2, n-2):
        diff = max(buildings[j - 2], buildings[j - 1], buildings[j + 1], buildings[j + 2])
        if buildings[j] > diff:
            result += (buildings[j] - diff)
    print('#%d %d' %(i, result))




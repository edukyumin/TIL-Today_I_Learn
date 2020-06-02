import sys
sys.stdin=open('Algo1_서울_3_이규민.txt', 'r')
def func():
    global N, arr
    for i in range(N):
        empty_arr=[0]*10
        for j in range(10):
            if arr[j] != 0:
                #절대값 10미만의 수에 대해
                if abs(arr[j]) <10:
                    #양수면
                    if arr[j]>=0:
                        #경계가아니라면
                        if j+1 != 10:
                            #다음께 0이면 그대로 복사
                            if empty_arr[j+1] == 0:
                                empty_arr[j+1] = arr[j]
                            #0이아니면 그 자리수와 더하기
                            else:
                                empty_arr[j+1] = arr[j+1] + arr[j]
                        #경계면 그 수에 음수
                        else: empty_arr[j] = -arr[j]
                    #음수일떄
                    if arr[j]<0:
                        #경계가 아니라면
                        if j-1 !=-1:
                            #전꺼가 0이면 그대로 복사
                            if empty_arr[j-1] == 0:
                                empty_arr[j-1] = arr[j]
                            #0이면 더하기
                            else:
                                empty_arr[j-1] = empty_arr[j-1] + arr[j]
                        #경계라면 그 수에 음수부호
                        else:
                            empty_arr[j] = -arr[j]
                #10이상의 수인경우
                else:
                    # 경계가 아니라면
                    if j + 1 != 10 and j -1 != -1:
                        # 다음께 0이면
                        if arr[j+1] == 0:
                            #그 다음수 는 절대값 반절
                            empty_arr[j+1] = abs(arr[j])//2
                        # 다음께 0이 아니라면
                        else:
                            empty_arr[j+1] = arr[j+1] + abs(arr[j])//2
                        # 그전께 0이면
                        if empty_arr[j-1] == 0:
                            empty_arr[j-1] = -abs(arr[j])//2
                        # 그전꼐 0이 아니라면
                        else:
                            empty_arr[j-1] = empty_arr[j-1] - abs(arr[j])//2
                    #9번째 칸이라면
                    elif j+1 ==10 :
                        empty_arr[j] = -abs(arr[j])//2
                        if empty_arr[j - 1] == 0:
                            empty_arr[j - 1] = -abs(arr[j]) // 2
                        else:
                            empty_arr[j - 1] = empty_arr[j - 1] - abs(arr[j])//2
                    #0번째 칸이라면
                    elif j-1 ==-1 :
                        empty_arr[j] = abs(arr[j])//2
                        if arr[j+1] == 0:
                            empty_arr[j+1] = abs(arr[j])//2
                        else:
                            empty_arr[j+1] = arr[j+1] + abs(arr[j])//2
        arr = empty_arr
    result= ''
    for i in range(10):
        if i != 9:
            result+=str(arr[i]) + ' '
        else:
            result+=str(arr[i])
    return result
testcase = int(input())
for i in range(1, testcase+1):
    N = int(input())
    arr = list(map(int, input().split()))
    print('#{} {}'.format(i, func()))
# 10개의 정수를 입력받아 부분집합의 합이 0이 되는 것이 존재하는지를 계산하는 함수를 작성하라
arr = [-5, -4, -2, -1, 0, 2, 3, 4, 1, 5]
print(arr)

n = len(arr)  #n: 원소의 개수 10개

for i in range(1, 1<<n) : # 1<<n : 부분 집합의 개수 2의10승  #0부터로 안하고 1부터해서 공집합은 빼준것
    result = []
    for j in range(n): #원소의 수만큼 비트를 비교함 10개
        if i & (1<<j):  # i의 j번쨰 비트가 1 이면 j번쨰 원소 출력
            result.append(arr[j])

    if sum(result) == 0:
        print(result)


##정렬
###버블정렬
# numbers = [55, 7 ,78, 12, 42]
# sorted_numbers = []
# for number in numbers:
#     sorted_numbers.append(number)
#     print(sorted_numbers)
#     print(len(sorted_numbers))
#     if len(sorted_numbers) != 1:
#         if sorted_numbers[-2] >sorted_numbers[-1]:
#             sorted_numbers[-2], sorted_numbers[-1] = sorted_numbers[-1], sorted_numbers[-2]
#     print('-------')
#     print(sorted_numbers)

###선생님 코드
def BubbleSort(a):  # 정렬할 리스트
    for i in range(len(a) - 1, 0, -1):  # 범위의 끝 위치
        for j in range(0, i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


print(BubbleSort([55, 7, 78, 12, 42]))

##카운팅 정렬
def Counting_Sort(A, B, k):
# A [1,...] --입력된 배열
# B [1,...] --정렬된 배열
# C [1,...] --카운트 배열
    C = [0] * k
    for i in range(0, len(B)) :
        C[A[i]] += 1
    for i in range(1, len(C)):
        C[i] += C[i-1]
    for i in range(len(B)-1, -1, -1):
        B[C[A[i]]-1] = A[i]
        C[A[i]] -= 1
    return B

print(Counting_Sort([55, 7, 78, 12, 42], [0, 0, 0, 0, 0], 80))

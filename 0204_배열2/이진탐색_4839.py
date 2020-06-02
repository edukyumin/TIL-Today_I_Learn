import sys
sys.stdin = open('이진탐색_4839.txt', 'r')

testcase = int(input())

for i in range(1, testcase + 1):
    high, page_a, page_b = list(map(int, input().split()))
    # print(high)
    # print(page_a)
    low = 1
    count_a = 0
    h = high

    for a in range(h):
        half = (low + h)//2
        if half == page_a :
            count_a += 1
            break
        else:
            if half > page_a:
                h = half
            elif half < page_a:
                low = half
            count_a += 1

    h = high
    low = 1
    count_b = 0

    for b in range(h):
        half = (low + h) // 2
        if half == page_b :
            count_b += 1
            break
        else:
            if half > page_b:
                h = half
            elif half < page_b:
                low = half
            count_b += 1

    if count_a > count_b:
        print('#{} B'.format(i))
        # print(count_a, count_b)
    elif count_a < count_b:
        print('#{} A'.format(i))
        # print(count_a, count_b)
    elif count_a == count_b:
        print('#{} 0'.format(i))
        # print(count_a, count_b)












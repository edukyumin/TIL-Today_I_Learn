import sys
sys.stdin = open('flatten.txt', 'r')

test_case=10

for i in range(1, test_case+1):
    dump_chance = int(input())
    boxes = list(map(int, input().split()))
    boxes.sort()


    for j in range(dump_chance):
        if boxes[-1] - boxes[0] >1:
            boxes[-1] -= 1
            boxes[0] += 1
        else:
            break
        boxes.sort()
    print('#%d %d' %(i, boxes[-1]- boxes[0]))

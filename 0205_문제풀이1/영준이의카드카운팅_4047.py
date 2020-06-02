import sys
sys.stdin = open('영준이의카드카운팅_4047.txt', 'r')

def Counting(card):
    result = []
    for i in range(len(card)//3):
        new_card = card[3*i:3*i +3]
        if new_card in result:
            return 'ERROR'
        else:
            result.append(new_card)
    result.sort()
    count_C, count_D, count_H ,count_S = (0, 0, 0, 0)

    for j in range(len(result)):
        if result[j][0] == 'C':
            count_C += 1
        elif result[j][0] == 'D':
            count_D += 1
        elif result[j][0] == 'H':
            count_H += 1
        elif result[j][0] == 'S':
            count_S += 1
    need = [str(13 - count_S), str(13 - count_D), str(13 - count_H), str(13 - count_C)]
    needs = ' '.join(need)
    return needs

testcase = int(input())
for i in range(1, testcase + 1):
    print('#{} {}'.format(i, Counting(input())))
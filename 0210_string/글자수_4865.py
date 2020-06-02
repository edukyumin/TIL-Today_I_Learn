import sys
sys.stdin = open('글자수_4865.txt', 'r')

def func():
    my_dic = {}
    for i in range(len(str1)):
        my_dic[str1[i]] = 0

    for j in range(len(str2)):
        if str2[j] in my_dic:
            my_dic[str2[j]] += 1



    return max(my_dic.values())

testcase = int(input())
for i in range(1, testcase+1):
    str1 = input()
    str2 = input()
    print('#{} {}'.format(i, func()))
import sys
sys.stdin = open('다솔이의다이아몬드장식_4751.txt', 'r')

def diamond(letter):
    n = 4 * len(letter) +1
    empty_list = [['.' for i in range(n)] for i in range(5)]
    for i in range(5):
        # 첫째줄, 다섯째줄
        if i == 0 or i == 4:
            for j in range(2, n, 4):
                empty_list[i][j] = '#'
        #둘쨰줄, 넷째줄
        if i ==1 or i ==3:
            for j in range(1, n, 2):
                empty_list[i][j] = '#'

        #셋째줄
        if i ==2:
            for j in range(0,n,4):
                empty_list[i][j] = '#'

            for j in range(2, n, 4):
                z= (j-2)//4
                empty_list[i][j] = letter[z]
    my_str = ''
    for k in empty_list:
        my_str += ''.join(k) +'\n'

    return my_str[:-1]

testcase = int(input())
for i in range(testcase):
    print(diamond(input()))
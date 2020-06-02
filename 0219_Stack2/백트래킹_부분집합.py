## 부분집합 구하기
S = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def backtrack(a, k, input, s):
    if s > 10: return

    if k == input:
        print(a)
        psum = 0
        for i in range(input):
            if a[i]:
                psum += S[i]
        if psum == 10:
            for i in range(input):
                if a[i]:
                    print(S[i], end=' ')
            print()
    else:
        a[k] = 1
        backtrack(a, k+1, input, s+S[k])
        a[k] = 0
        backtrack(a, k+1, input, s)

a = [0] * 10
backtrack(a, 0, 10, 0)
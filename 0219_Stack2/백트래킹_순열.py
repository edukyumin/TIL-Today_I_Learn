#순열
def backtrack(a, k, N):
    c = [0] * N
    if k == N:
        print(a)
    else:
        in_perm = [False] * N
        for i in range(k):
            idx = a[i]
            in_perm[idx] = True

        cand = 0
        for idx in range(N):
            if in_perm[idx] == False:
                c[cand] = idx
                cand += 1

        for i in range(cand):
            a[k] = c[i]
            backtrack(a, k+1, N)
a = [0] * 3
backtrack(a, 0, 3)
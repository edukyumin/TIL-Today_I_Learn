T = int(input())
for tc in range(1, T + 1):
    n, m = list(map(int, input().split()))
    cheese = list(map(int, input().split()))
    q = [[0, cheese[0]]]
    j = 0
    last = 0
    while len(q) > 0:
        if (len(q) < n) and (j < m - 1):
            j += 1
            q.append([j, cheese[j]])
        else:
            q[0][1] = q[0][1] // 2
            if q[0][1] == 0:
                w = q.pop(0)
                last = w[0]

            else:
                l = q.pop(0)
                q.append(l)

    print('#{} {}'.format(tc, last + 1))
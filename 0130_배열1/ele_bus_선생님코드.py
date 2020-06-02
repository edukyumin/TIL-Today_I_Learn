# 먼저 움직인 다음에 충전기를 찾음

import sys

sys.stdin = open('elec_bus.txt', 'r')

T = int(input())
T += 1
for tc in range(1, T):
    K,N,M = map(int, input().split())
    stops = [0] + list(map(int, input().split())) + [N] #출발점과 종점 번호 추가
    last = 0 # 마지막 충전기
    cnt = 0 # 충전 횟수
    next = last +K
    for i in range (1, M+2):
        if (stops[i] - stops [i-1]) > K: #충전기 사이가 K보다 멀때
            cnt = 0
            break
        if stops[i] > next:             # i 번 충전기까지 갈 수 없으면
            last = stops[i-1]           # 이전 충전기에서 충전
            cnt += 1
        next = last + K
    print( '#%d %d' % (tc, cnt))
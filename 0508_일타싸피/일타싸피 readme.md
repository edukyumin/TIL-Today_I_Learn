# 일타싸피 코드

- 힘당구로 당구게임을 짜보았다
- 일단 무조건 세게 때리면 언젠가는 구멍과 일직선이 돼지않을까?
  - 그때 힘을 조절해서 떄려보자!!!
- 조금더 효율적인 (각도를 고려한) 코드를 짤 수 있을까?

```python
def play(conn, gameData):
    # angle = float(input("각도 입력: "))
    # power = float(input("파워 입력: "))
    ######################################################################################
    # 각도 계산하기
    print('여기임')
    print(gameData.balls)
    for i in range(1, 5):
        if gameData.balls[i][0] != -1:
            break
    dx = gameData.balls[i][0] - gameData.balls[0][0]
    dy = gameData.balls[i][1] - gameData.balls[0][1]
    if dx > 0 and dy >= 0: # 1사분면일 경우
        angle = 90 - math.degrees(math.atan(dy / dx)) +1
    elif dx > 0 and dy < 0: # 2사분면일 경우
        angle = 90 - math.degrees(math.atan(dy / dx)) +1
    elif dx < 0 and dy < 0: # 3사분면일 경우
        angle = 270 - math.degrees(math.atan(dy / dx)) +1
    else: # dx < 0 and dy > 0 4사분면일 경우
        angle = 270 - math.degrees(math.atan(dy / dx)) +1
    # 파워 계산하기
    for j in range(6):
        goal = [[0, 127],[127,127],[254,127],[0,0],[127,0],[254,0]]
        dx2 = goal[i][0] - gameData.balls[0][0]
        dy2 = goal[i][1] - gameData.balls[0][1]
        if dy2/dx2 == dy/dx:
            power = math.sqrt(dx ** 2 + dy ** 2) / 2
            break
    else:
        power = 100
    ######################################################################################
    conn.send(angle, power)
```


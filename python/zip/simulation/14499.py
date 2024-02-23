import sys
input = sys.stdin.readline

n, m, x, y ,k = map(int, input().split())
Map = []

for _ in range(n):
    Map.append(list(map(int, input().split())))

dice = [[0 for _ in range(4)] for _ in range(2)]

upDownP, rightLeftP = 3, 3
order = list(map(int, input().split()))

mapMove = [(0, 0), (0, 1), (0, -1), (-1, 0), (1, 0)]
pointerMove = [(0, 0, 0), (1, 0, -1), (1, 0, 1), (0, 1, 0), (0, -1, 0)]

for ord in order:
    nx = x + mapMove[ord][0]
    ny = y + mapMove[ord][1]

    if 0 <= nx < n and 0 <= ny < m: # 지도 범위 내에 있는지
        # 밑면을 가르키는 포인터값 update
        row, dx, dy = pointerMove[ord]
        upDownP = (upDownP + dx) % 4
        rightLeftP = (rightLeftP + dy) % 4

        # Map값, 밑면 값 update
        if Map[nx][ny] == 0:
            if ord == 1 or ord == 2:
                Map[nx][ny] = dice[1][rightLeftP]
            else:
                Map[nx][ny] = dice[0][upDownP]
        
        else:
            dice[0][upDownP] = Map[nx][ny]
            dice[1][rightLeftP] = Map[nx][ny]
            Map[nx][ny] = 0

        # 밑면, 윗변값 동기화
        if ord == 1 or ord == 2:
            dice[0][upDownP] = dice[1][rightLeftP]
            dice[0][(upDownP + 2) % 4] = dice[1][(rightLeftP + 2) % 4]
        else:
            dice[1][rightLeftP] = dice[0][upDownP]
            dice[1][(rightLeftP + 2) % 4] = dice[0][(upDownP + 2) % 4]

        x = nx
        y = ny

        print(dice[0][(upDownP + 2) % 4])
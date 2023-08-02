#nba 농구

import sys
n = int(input())
goals = []
score = [[0, 0], [0, 0], [0, 0]] # score, time
clock = 0

for i in range(n+1):
    if i < n:
        team, time = sys.stdin.readline().split()
        m, s = map(int, time.split(":"))
        tmp = m*60 + s
    else:
        tmp = 48 * 60

    win = lose = 0
    if score[1][0] > score[2][0]:
        win = 1
        lose = 2
    elif score[1][0] < score[2][0]:
        win = 2
        lose = 1
    
    if win != 0 and lose != 0:
        score[win][1] += tmp - clock
    clock = tmp

    if i < n+1:
        score[int(team)][0] += 1

for i in range(1,3):
    h = score[i][1] // 60 
    h = str(h) if h >= 10 else "0"+str(h)
    m = score[i][1] % 60
    m = str(m) if m >= 10 else "0"+str(m)
    print(h+":"+m)
    




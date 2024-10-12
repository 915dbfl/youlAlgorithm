# 22분
import sys
input = sys.stdin.readline

tc = int(input())
play = [False] * 11
answer = 0

def dfs(position, total):
    global answer
    if position == 11:
        answer = max(answer, total)
        return
    
    for i in range(11):
        if level[position][i] > 0 and not play[i]:
            play[i] = True
            dfs(position+1, total + level[position][i])
            play[i] = False

for _ in range(tc):
    answer = 0
    # 부루트 포스 + 백 트래킹
    playerLevel = [list(map(int, input().split())) for _ in range(11)]
    level = list(zip(*playerLevel))

    dfs(0, 0)

    print(answer)
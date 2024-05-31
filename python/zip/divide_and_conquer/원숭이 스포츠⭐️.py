import sys
input = sys.stdin.readline

team = ['A', 'B']

def dfs(l, r, day, t):
    if day == 7: return
    mid = (l + r)//2

    for i in range(l, r+1):
        answer[day][i] = team[t] if i <= mid else team[t^1]
    
    dfs(l, mid, day + 1, t)
    dfs(mid+1, r, day+1, t^1)

n = int(input())
answer = [[""] * n for _ in range(7)]

dfs(0, n-1, 0, 0)

for i in range(7):
    print("".join(answer[i]))
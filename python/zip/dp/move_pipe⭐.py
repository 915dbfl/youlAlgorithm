# #22.12.20
# #파이프 옮기기1
# #class4/골드5

# #dfs: 시간초과
# import sys
# input = sys.stdin.readline

# n = int(input())
# dif = [[(0, 1), (1, 1)], [(1, 0), (1, 1)], [(0, 1), (1, 0), (1, 1)]]
# house = [list(map(int, input().split())) for _ in range(n)]
# check_x = [house[i][-1] for i in range(n)]

# answer = 0
# def dfs(y, x, type):
#   global answer

#   if type == 2 and (y == (n-1) or x == (n-1)):
#     if y == (n-1) and sum(house[-1][x:n]) == 0:
#       answer += 1
#       return
#     if x == (n-1) and sum(check_x[y:n]) == 0:
#       answer += 1
#       return

#   for dy, dx in dif[type]:
#     ny = y + dy
#     nx = x + dx
#     if 0<= ny < n and 0<= nx < n and house[ny][nx] != 1:
#       if dy == 1 and dx == 1:
#         if ny >= 1:
#           if house[ny-1][nx] == 1:
#             continue
#         if nx >= 1:
#           if house[ny][nx-1] == 1:
#             continue
#         dfs(ny, nx, 2)
#       elif dy == 0:
#         dfs(ny, nx, 0)
#       else:
#         dfs(ny, nx, 1)

# dfs(0, 1, 0)
# print(answer)

# # dfs 리팩토링
# import sys
# input = sys.stdin.readline

# n = int(input())
# house = [list(map(int, input().split())) for _ in range(n)]

# answer = 0
# def dfs(y, x, type):
#   global answer

#   if y == n-1 and x == n-1 and house[y][x] != 1:
#     answer += 1
#     return

#   if type != 1:
#     if x < n-1 and house[y][x+1] != 1:
#       dfs(y, x+1, 0)
#   if type != 0:
#     if y < n-1 and house[y+1][x] != 1:
#       dfs(y+1, x, 1)
#   if x < n-1 and y < n-1:
#     if house[y+1][x] != 1 and house[y][x+1] != 1 and house[y+1][x+1] != 1:
#       dfs(y+1, x+1, 2)

# dfs(0, 1, 0)
# print(answer)

# dp
import sys
input = sys.stdin.readline

n = int(input())
house = [list(map(int, input().split())) for _ in range(n)]
dp = [[[0, 0, 0] for _ in range(n)] for _ in range(n)]

dp[0][1][0] = 1

for i in range(n):
  for j in range(2, n):
    if house[i][j] == 0:
      if i >= 1:
        dp[i][j][1] += dp[i-1][j][1] + dp[i-1][j][2]
        if house[i-1][j] == 0 and house[i][j-1] == 0:
          dp[i][j][2] += sum(dp[i-1][j-1])
      dp[i][j][0] += dp[i][j-1][0] + dp[i][j-1][2]

print(sum(dp[-1][-1]))
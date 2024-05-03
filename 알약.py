import sys
input = sys.stdin.readline

# arr[i][j]는 W가 i만큼 있고 H가 j만큼 있는 가지수
# dp 활용

# 풀이 1: 논리적인 디피 구하기
# 1) n = 3일 때 
    # 1. h가 0일 떄, 무조건 w를 먹어야 한다.
        # dp[i][j] = dp[i-1][j+1]
    # 2. h가 한 개라도 있을 때
        # h를 먹는 경우 -> dp[i][j-1]
        # w를 먹는 경우 -> dp[i-1][j+1]
        # => dp[i][j] = dp[i][j-1] + dp[i-1][j+1]
arr = [[0] * 31 for _ in range(31)]

for i in range(1, 31):
    arr[0][i] = 1

for i in range(1, 31): # W의 개수
    for j in range(30): # H의 개수
        if j == 0: # W를 하나 먹은 후 H가 생긴 경우
            arr[i][j] = arr[i-1][j+1]
        else:
            arr[i][j] = arr[i-1][j+1] + arr[i][j-1]

while 1:
    n = int(input())

    if n == 0:
        break

    print(arr[n][0])

# 풀이 2: 단순 규칙 dp 구하기
arr = [[0] * 31 for _ in range(31)]

for i in range(1, 31):
    arr[0][i] = 1

for i in range(1, 31):
    for j in range(i, 31):
        arr[i][j] += arr[i-1][j] + arr[i][j-1]
        
while True:
    N = int(input())
    if N == 0:
        break
    print(arr[N][N])
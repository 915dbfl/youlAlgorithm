#21.08.04
n, m = map(int, input().split())
lst = []
#총 n+1행, m+1열의 값을 저장할 수 있는 리스트 생성
dp = [[0] *(m+1) for _ in range(n+1)]
for cnt in range(n):
  lst.append(list(map(int, input().split())))
for cnt1 in range(1, n+1):
  for cnt2 in range(1, m+1):
    # (1,1)부터 (cnt1, cnt2)까지 합한 값을 dp[cnt1][cnt2]에 저장
    dp[cnt1][cnt2] = dp[cnt1-1][cnt2] + dp[cnt1][cnt2-1] - dp[cnt1-1][cnt2-1] + lst[cnt1-1][cnt2-1]
k = int(input())
for _ in range(k):
  i,j,x,y = map(int, input().split())
  print(dp[x][y]-dp[x][j-1]-dp[i-1][y]+dp[i-1][j-1])
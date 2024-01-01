# 단순 이중 포문 -> 시간 초과..
import sys

n = int(sys.stdin.readline())
heights = list(map(int, sys.stdin.readline().split()))

dp = [1] * n
dp_reverse = [1] * n

for i in range(1, n):
  for j in range(i-1, -1, -1):
    if heights[i] > heights[j]:
      dp[i] = max(dp[i], dp[j]+1)
    if heights[-i-1] > heights[-j-1]:
      dp_reverse[-i-1] = max(dp_reverse[-i-1], dp_reverse[-j-1]+1)
      
result = 0
for i in range(n):
  if result < dp[i] + dp_reverse[i] - 1:
    result = dp[i] + dp_reverse[i] - 1

print(result)

# LogN -> 이분 탐색
# 헷갈렸던 부분
    # binary search로 idx를 구하고 해당 위치에 값을 추가하는 것이 아니라 해당 위치의 값을 바꾸는 방식
    # 왜 바꿔야 할까?
    # 결국 끝에 추가되지 않는 이상, 전체 길이가 커지지 않음. 그래서 값을 추가하지 않고 바꾸는 것!

import sys
import bisect # 이분 탐색

N = int(sys.stdin.readline())
heights = list(map(int, sys.stdin.readline().split()))

dp_front = [heights[0]] # 앞 쪽 기준 밟을 수 있는 돌의 유효한 오름차순 높이
dp_back = [heights[-1]] # 뒷 쪽 기준 밟을 수 있는 돌의 유효한 오름차순 높이
front_cnt = [1] * N # 앞에서 부터 밟은 돌의 갯수
back_cnt = [1] * N # 뒤에서 부터 밟은 돌의 갯수

# 앞 쪽 기준
for i in range(N):
    if heights[i] > dp_front[-1]:
        dp_front.append(heights[i])
        idx = len(dp_front)-1

    else:
        # 이분탐색을 이용하여 logN의 복잡도로 이전의 가장 큰 원소의 idx값을 찾는다.
        idx = bisect.bisect_left(dp_front, heights[i])
        dp_front[idx] = heights[i]

    front_cnt[i] = idx+1

# 뒷 쪽 기준
heights.reverse()

for i in range(N):
    if heights[i] > dp_back[-1]:
        dp_back.append(heights[i])
        idx = len(dp_back)-1
    else:
        # 이분탐색을 이용하여 logN의 복잡도로 이전의 가장 큰 원소의 idx값을 찾는다.
        idx = bisect.bisect_left(dp_back, heights[i])
        dp_back[idx] = heights[i]
        
    back_cnt[N-i-1] = idx+1

ans = 0
for i in range(N):
    ans = max(ans, front_cnt[i] + back_cnt[i])

print(ans-1) # 가장 높은 크기의 돌이 2번 밟히기 때문에 -1 을 한다.
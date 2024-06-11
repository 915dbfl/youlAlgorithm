# level2

# 누적합
# 테스트 케이스 4 계속 틀림
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
heights = [-1] + list(map(int, input().split())) + [-1]
rain = [0] * (n+2)
days = []
day_cnt = 0

for _ in range(m):
	day_cnt += 1
	s, e = map(int, input().split())
	rain[s] += 1
	rain[e+1] -= 1
	
	if day_cnt <= 3:
		days.append([s, e])
	else:
		days.sort()
		ts, te = days.pop(0)
		while days:
			ds, de = days.pop(0)
			if ds <= te:
				te = max(te, de)
			elif ds > te:
				rain[ts] -= 1
				rain[te+1] += 1
				ts, te = ds, de
		rain[ts] -= 1
		rain[te+1] += 1
		day_cnt = 1
		days = [[s, e]]
	
for i in range(1, n+1):
	rain[i] += rain[i-1]
	heights[i] += rain[i]
	print(heights[i], end = " ")
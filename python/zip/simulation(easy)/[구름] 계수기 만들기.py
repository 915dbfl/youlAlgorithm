# level2
# 20분

import sys
input = sys.stdin.readline

n = int(input())
max_lst = list(map(int, input().split()))
value = list(map(int, input().split()))
value[-1] += int(input())

for i in range(n-1, -1, -1):
	if value[i] > max_lst[i]:
		cnt = value[i] // (max_lst[i]+1)
		value[i] = (value[i] % (max_lst[i]+1))
		if i > 0:
			value[i-1] += cnt
	else:
		break

print("".join(map(str, value)))
# level2

import sys
input = sys.stdin.readline

n = int(input())
fact = 1
for i in range(2, n+1):
	fact *= i
	
while len(str(fact)) > 1:
	fact = sum(map(int, list(str(fact))))
	
print(fact)
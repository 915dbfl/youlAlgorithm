import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
weights = list(map(int, input().split()))
checkPrimeList = [True] * (n * 1000 + 1)
checkPrimeList[1] = False

# 에라토스테네스의 체
maxCheckNum = int((n * 1000) ** 0.5)
for i in range(2, maxCheckNum+1):
    if checkPrimeList[i]:
        for j in range(i*2, n*1000+1, i):
            checkPrimeList[j] = False

# 전체 순열 구하기
answer = set()
for case in combinations(weights, m):
    total = sum(case)
    if checkPrimeList[total]:
        answer.add(total)

sortedAnswer = sorted(answer)
print(*sortedAnswer if sortedAnswer else -1)
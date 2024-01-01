#22.12.14
#치킨 배달
#class4/골드5

# 그리디 알고리즘: 오답
# 그리디를 통해 남긴 치킨 집이 최선의 결과가 아니다.
import sys
from collections import defaultdict
input = sys.stdin.readline

n, m = map(int, input().split())
chicken = []
house = []

#집, 치킨집 위치 구하기
for i in range(1, n+1):
  for idx, val in enumerate(list(map(int, input().split()))):
    if val == 2:
      chicken.append((i, idx+1))
    elif val == 1:
      house.append((i, idx+1))

#남겨야할 치킨집 구하기
chicken_dis = defaultdict(list)
for c in chicken:
  for h in house:
    dis = abs(c[0]-h[0]) + abs(c[1]-h[1])
    chicken_dis[c].append(dis)
print(chicken_dis)

if len(chicken) != m:
  lst = sorted(chicken_dis.keys(), key = lambda x: sum(chicken_dis[x]))[:m]
  lst = list(map(lambda x: chicken_dis[x], lst))
else:
  lst = chicken_dis.values()

#도시의 최소 치킨 거리 구하기
answer = 0
for c in zip(*lst):
  answer += min(c)

print(answer)

# 조합 사용
import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
city = list(list(map(int, input().split())) for _ in range(n))
chicken = []
house = []

for i in range(n):
  for j in range(n):
    if city[i][j] == 1:
      house.append((i, j))
    elif city[i][j] == 2:
      chicken.append((i, j))

answer = 2*n*len(house)
for case in combinations(chicken, m):
  tmp = 0
  for h in house:
    tmp += min([abs(h[0]-c[0])+abs(h[1]-c[1]) for c in case])
    if tmp >= answer:
      break

  answer = min(answer, tmp)

print(answer)
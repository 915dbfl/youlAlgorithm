# 누적합
import sys
input = sys.stdin.readline

n = int(input())
villages = []
pprefix = [0] * n
dist = [0] * n

for i in range(n):
    villages.append(list(map(int, input().split())))

# villages가 정렬되지 않은 순으로 들어올 수 있음 주의⭐️
villages.sort()
pprefix[0] = villages[0][1]
for i in range(1, n):
    pprefix[i] += pprefix[i-1] + villages[i][1]

# 위치 0에 우체국을 세울 경우 거리 총합
for i in range(1, n):
    vidx, vpcnt = villages[i]
    dist[0] += abs(villages[0][0] - vidx) * vpcnt

# dp 구하기
minDist = dist[0]
minIdx = villages[0][0]
for i in range(1, n):
    diff_dist = abs(villages[i][0] - villages[i-1][0])
    dist[i] = dist[i-1]
    dist[i] -= diff_dist * (pprefix[-1] - pprefix[i-1])
    dist[i] += diff_dist * pprefix[i-1]
    if dist[i] < minDist:
        minDist = dist[i]
        minIdx = villages[i][0]

print(minIdx)

# 중앙값: 전체 인구수의 절반이 넘어가는 지점
import sys

input = sys.stdin.readline
n = int(input())
villages = []
total_population = 0

for _ in range(n):
    idx, pcnt = map(int, input().split())
    villages.append((idx, pcnt))
    total_population += pcnt

villages.sort()

prefix_population = [0] * n
prefix_population[0] = villages[0][1]
for i in range(1, n):
    prefix_population[i] = prefix_population[i-1] + villages[i][1]

for i in range(n):
    if prefix_population[i] >= (total_population + 1) // 2:  # (total_population + 1) // 2는 홀수 인구수 처리를 위함
        print(villages[i][0])
        break
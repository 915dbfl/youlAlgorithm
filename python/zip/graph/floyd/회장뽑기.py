import sys
input = sys.stdin.readline
INF = sys.maxsize

n = int(input())

# 서로 친구인 회원들 입력 받기
## 플로이드 워샬에 사용할 거리 배열
dist = [[INF] * (n+1) for _ in range(n+1)]
a, b = map(int, input().split())
while a != -1 and b != -1:
    dist[a][b] = 1
    dist[b][a] = 1
    a, b = map(int, input().split())

for i in range(1, n+1):
    dist[i][i] = 0

# 플로이드 워샬 => O(50 * 50 * 50)
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j: continue
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

lead, score = -1, INF
candi = []
for i in range(1, n+1):
    # 친구와의 거리 최대값 = 회원 점수
    Max = -1
    for j in range(1, n+1):
        if dist[i][j] != INF:
            Max = max(Max, dist[i][j])

    if score > Max:
        lead, score = i, Max
        candi = []
    elif score == Max:
        candi.append(i)

candi.append(lead)
candi.sort()

print(score, len(candi))
print(" ".join(map(str, candi)))
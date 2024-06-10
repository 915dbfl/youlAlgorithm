# 모든 위치에서 빗물이 고일 수 있는지 확인
# 고일 수 있는 빗물 합계
h, w = map(int, input().split())
world = list(map(int, input().split()))

ans = 0
for i in range(1, w-1):
    left_max = max(world[:i])
    right_max = max(world[i+1:])

    compare = min(left_max, right_max)
    if world[i] < compare:
        ans += compare - world[i]

print(ans)
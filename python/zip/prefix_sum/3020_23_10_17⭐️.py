# 23.10.17 개똥벌레

# 풀이법: 누적합
# 종유석, 석순 배열은 각각 h+1개의 배열을 가지고 있는다.
# 입력을 받으며, 종유석/석순일 때 해당 배열, 해당 값에 +1을 해준다.
# h+1, 0까지 반복문을 돌리며 다음의 과정을 반복한다.
    # i번째 높이 종유석의 개수는 i+1 종유석의 개수를 포함한다.
# 1, h까지 반복문을 돌리면서 다음의 과정을 반복한다.
    # 높이 i에서 종유석과 석순의 개수는 down[i] + up[h-i+1]개 이다.
    # 만약 해당 값이 min값보다 작다면 갱신해준다.
    # 만약 해당 값이 min값과 동일하다면 count + 1해준다.

n, h = map(int, input().split())

down = [0] * (h + 1)  # 석순
up = [0] * (h + 1)  # 종유석

min_count = n  # 파괴해야 하는 장애물의 최소값
range_count = 0  # 최소값이 나타나는 구간의 수

for i in range(n):
    if i % 2 == 0:
        down[int(input())] += 1
    else:
        up[int(input())] += 1

for i in range(h-1, -1, -1):
    down[i] += down[i+1]
    up[i] += up[i+1]

for i in range(1, h+1):
    if min_count > down[i] + up[h-i+1]:
        min_count = down[i] + up[h-i+1]
        range_count = 1
    elif min_count == down[i] + up[h-i+1]:
        range_count += 1

print(min_count, range_count)
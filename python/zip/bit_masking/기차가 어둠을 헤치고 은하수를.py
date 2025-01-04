import sys
input = sys.stdin.readline

n, m = map(int, input().split())
# n개의 기차 초기값 저장
trains = [0 for _ in range(n)]
# 명령 입력 받기
for i in range(m):
    order = list(map(int, input().split()))
    train_idx = order[1]-1
    if order[0] == 1:
        trains[train_idx] |= (1 << order[2]-1)
    elif order[0] == 2:
        trains[train_idx] &= ~(1 << order[2]-1)
    elif order[0] == 3:
        trains[train_idx] <<= 1
        trains[train_idx] &= ~(1 << 20)
    else:
        trains[train_idx] >>= 1

print(len(set(trains)))
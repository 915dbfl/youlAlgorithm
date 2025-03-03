"""
# 주요 정보
- 트리
- 각 정점에는 박스가 존재 -> 박스 안에는 비어 있거나 몇 개의 구슬을 포함
- 모든 박스에 1개의 구슬이 들어있도록 최소한으로 움직이기

# 풀이 과정
1. 루트 구하기
2. 루트를 시작으로 자식트리에서 가지고 있는 비즈 수 루트에 기록
3. 필요한 비즈 수와의 차이 합 구하기
"""

import sys
from collections import defaultdict
input = sys.stdin.readline

degree = []
beads_cnt = []
childs_cnt = []
childs = defaultdict(list)

def dfs(cur):
    if len(childs[cur]) == 0:
        return beads_cnt[cur], childs_cnt[cur]
    
    for nxt in childs[cur]:
        child_beads, child_childs = dfs(nxt)
        beads_cnt[cur] += child_beads
        childs_cnt[cur] += child_childs

    return beads_cnt[cur], childs_cnt[cur]
    
while 1:
    n = int(input())
    degree = [0] * (n+1)
    beads_cnt = [0] * (n+1)
    childs_cnt = [1] * (n+1)
    childs = defaultdict(list)
    root = -1

    if n == 0:
        break
    else:
        for _ in range(n):
            infos = list(map(int, input().split()))
            beads_cnt[infos[0]] = infos[1]
            if infos[2] > 0:
                childs[infos[0]] = infos[3:]
                for ch in infos[3:]:
                    degree[ch] += 1

    # 루트 찾기
    for i in range(1, n+1):
        if degree[i] == 0:
            root = i
            break

    # 각 트리마다 가지고 있는 비즈 수 및 전체 자식 수 구하기
    dfs(root)

    answer = 0
    for i in range(1, n+1):
        answer += abs(childs_cnt[i] - beads_cnt[i])

    print(answer)
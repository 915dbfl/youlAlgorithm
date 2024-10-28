# dfs, 브루트포스
# 40분

import sys
input = sys.stdin.readline

k = int(input())
weights = list(map(int, input().split()))

left, right = 0, 0
totalWeight = sum(weights)
canMake = [False] * (totalWeight + 1)

def dfs(cur):
    global left, right
    if cur == k: return

    curWeight = weights[cur]
    canMake[curWeight] = True
    dfs(cur + 1)

    right += curWeight
    canMake[right] = True

    if right - left > 0:
        canMake[right - left] = True
    dfs(cur + 1)
    
    right -= curWeight
    left += curWeight
    canMake[left] = True

    if right - left > 0:
        canMake[right - left] = True
    dfs(cur + 1)
    left -= curWeight

dfs(0)
print(totalWeight - sum(canMake))

# 더 간단한 풀이
k = int(input())
lst = list(map(int, input().split()))

used = [0] * (sum(lst) + 1)

def dfs(level, total):
    if level == k:
        if total >= 0:
            used[total] = 1
        return
    
    for nxt in (total, total + lst[level], total - lst[level]):
        dfs(level+1, nxt)

dfs(0, 0)

print(used.count(0))
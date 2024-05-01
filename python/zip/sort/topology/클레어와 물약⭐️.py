from collections import deque
import sys

# 위상정렬
# 풀이과정
# 핵심: 레시피의 차수를 가지고 위상 정렬을 진행함
    # 레시피의 차수는 레시피가 필요로 하는 물약의 개수를 나타낸다.

input = sys.stdin.readline
n, m = map(int, input().split())

visited = [False] * (n+1)
nxt_recipe = [[] for _ in range(n+1)]
indegree = [0] * (m+1) # 레시피 차수를 저장
recipe_info = []

q = deque()
# O(n*m) = O(200000 * 200000)
for j in range(m):
    inputs = list(map(int, input().split()))

    # i 물약을 필요로 하는 물약 저장
    for i in range(1, len(inputs) - 1):
        nxt_recipe[inputs[i]].append(j)
        # 해당 레시피가 필요로 하는 물약의 차수 업데이트
        indegree[j] += 1

    recipe_info.append(inputs[1:])

l = int(input())
result = list(map(int, input().split()))

# 가지고 있는 물약 레시피 차수에서 빼주기
for liquid in result:
    visited[liquid] = True

    # liquid를 필요로 하는 레시피 차수 뺴주기
    for next in nxt_recipe[liquid]:
        indegree[next]-= 1
        if indegree[next]== 0:
            # 차수가 0인 레시피를 queue에 넣기
            q.append(recipe_info[next])

while q:
    r_info = q.popleft()

    visited[r_info[-1]] = True
    result.append(r_info[-1])

    for next in nxt_recipe[r_info[-1]]:
        indegree[next] -= 1
        if indegree[next] == 0 and not visited[next]:
            q.append(recipe_info[next])

print(len(result))
print(" ".join(map(str, sorted(result))))
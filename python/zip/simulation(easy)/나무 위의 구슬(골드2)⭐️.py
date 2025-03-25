"""
풀이 과정
- 구슬 규칙
1. 리프 노드 - 무조건 자기 자신 반환
2. 자식이 하나 - 무조건 해당 자식 반환
3. 자식이 둘
    - k % 2 == 1: 왼쪽으로 이동
    - k % 2 == 0: 오른쪽으로 이동
"""

# 반복문 풀이
import sys
input = sys.stdin.readline

N = int(input())
children = [[0, 0]] + [list(map(int, input().split())) for _ in range(N)]
K = int(input())

node = 1
while True :
  if children[node][0] == children[node][1] == -1 :
    print(node)
    break
  if children[node][0] == -1 :
    node = children[node][1]
  elif children[node][1] == -1 :
    node = children[node][0]
  else :
    if K % 2:
        node, K = children[node][0], K // 2 + 1
    else:
        node, K = children[node][1], K // 2
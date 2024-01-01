#22.11.10
#이중 우선순위 큐
#calss3/골드4
#최대힙, 최소힙

import sys
from collections import defaultdict
from heapq import heappush, heappop
input = sys.stdin.readline

t = int(input())
for _ in range(t):
  k = int(input())

  min_heap = []
  max_heap = []
  dic = defaultdict(int)
  cnt = 0

  for _ in range(k):
    op, val = input().split()

    if op == "I":
      heappush(min_heap, int(val))
      heappush(max_heap, (-int(val), int(val)))
      dic[int(val)] += 1
      cnt += 1

    elif cnt > 0:
      if val == "-1": #최솟값 삭제
        tmp = heappop(min_heap)
        
        while dic[tmp] < 1:
          tmp = heappop(min_heap)
        
        dic[tmp] -= 1

      else: #최댓값 삭제
        tmp = heappop(max_heap)

        while dic[tmp[1]] < 1:
          tmp = heappop(max_heap)

        dic[tmp[1]] -= 1

      cnt -= 1

  if cnt <= 0:
    print("EMPTY")
  else:
    min_num = heappop(min_heap)
    max_num = heappop(max_heap)

    while dic[min_num] < 1:
      min_num = heappop(min_heap)
    
    while dic[max_num[1]] < 1:
      max_num = heappop(max_heap)

    print(max_num[1], min_num)

# 값마다 인덱스를 부여해 최대힙, 최소힙 동기화 (공간복잡도 줄인 풀이)
import sys
from heapq import heappush, heappop
input = sys.stdin.readline

t = int(input())
for _ in range(t):
  k = int(input())

  min_heap = []
  max_heap = []
  visited = [False] * k

  for j in range(k):
    op, val = input().split()

    if op == "I":
      heappush(min_heap, (int(val), j))
      heappush(max_heap, (-int(val), j))
      visited[j] = True

    else:
      if val == "-1": #최솟값 삭제
        while min_heap and not visited[min_heap[0][1]]:
          heappop(min_heap)
        if min_heap:
          visited[min_heap[0][1]] = False
          heappop(min_heap)
      else: #최댓값 삭제
        while max_heap and not visited[max_heap[0][1]]:
          heappop(max_heap)
        if max_heap:
          visited[max_heap[0][1]] = False
          heappop(max_heap)

  while min_heap and not visited[min_heap[0][1]]:
    heappop(min_heap)

  while max_heap and not visited[max_heap[0][1]]:
    heappop(max_heap)

  if not min_heap or not max_heap:
    print("EMPTY")
  else:
    print(-max_heap[0][0], min_heap[0][0])
#2022.03.12
#더 맵게

#remove를 이용한 풀이(시간초과)
def solution(scoville, K):
  answer = 0
  while min(scoville) < K:
    if len(scoville) == 1:
      return -1
    tmp1 = min(scoville)
    scoville.remove(tmp1)
    tmp2 = min(scoville)
    scoville.remove(tmp2)
    scoville.append(tmp1 + tmp2 * 2)
    answer += 1   
  return answer

#heap을 이용한 풀이 (best)
from heapq import heappush, heappop, heapify

def solution(scoville, K):
  answer = 0
  heap = heapify(scoville)
  while scoville[0] < K:
    if len(scoville) == 1:
      return -1
    tmp = heappop(scoville) + heappop(scoville) * 2
    heappush(scoville, tmp)
    answer += 1
  return answer
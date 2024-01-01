#22.10.23
#차이를 최대로
#실버2
#브루트 포스

#풀이
from collections import deque

n = int(input())
lst = list(map(int, input().rstrip().split()))

dq = deque(sorted(lst))
a = dq.popleft()
b = a
answer = 0

while dq:
  if abs(a-dq[0]) > abs(a-dq[-1]):
    tmp_a = "s"
  else:
    tmp_a = "e"
  if abs(b-dq[0]) > abs(b-dq[-1]):
    tmp_b = "s"
  else:
    tmp_b = "e"
  
  if tmp_b == "s" and tmp_a == "s":
    if abs(a-dq[0]) > abs(b-dq[0]):
      answer += abs(a-dq[0])
      a = dq.popleft()
    else:
      answer += abs(b-dq[0])
      b = dq.popleft()
  elif tmp_a == "s":
    if abs(a-dq[0]) > abs(b-dq[-1]):
      answer += abs(a-dq[0])
      a = dq.popleft()
    else:
      answer += abs(b-dq[-1])
      b = dq.pop()
  elif tmp_b == "s":
    if abs(a-dq[-1]) > abs(b-dq[0]):
      answer += abs(a-dq[-1])
      a = dq.pop()
    else:
      answer += abs(b-dq[0])
      b = dq.popleft()
  else:
    if abs(a-dq[-1]) > abs(b-dq[-1]):
      answer += abs(a-dq[-1])
      a = dq.pop()
    else:
      answer += abs(b-dq[-1])
      b = dq.pop()
  
print(answer)

#브루트 포스 - 재귀/백트래킹
#불필요한 탐색은 하지 않는 것이 dfs랑 차이점이다.
n = int(input())
nums = list(map(int, input().split()))
visited = [False]*n
answer = 0

def getAnswer(lst):
  global answer
  if len(lst) == n:
    tmp = 0
    for i in range(n-1):
      tmp += abs(lst[i]-lst[i+1])
    answer = max(answer, tmp)
    return

  for i in range(n):
    if visited[i] == False:
      visited[i] = True
      getAnswer(lst + [nums[i]])
      visited[i] = False

getAnswer([])
print(answer)

#브루트 포스 - 순열
from itertools import permutations

n = int(input())
nums = list(map(int, input().split()))
answer = 0

for case in permutations(nums):
  tmp = 0
  for i in range(n-1):
    tmp += abs(case[i]-case[i+1])
  answer = max(answer, tmp)

print(answer)
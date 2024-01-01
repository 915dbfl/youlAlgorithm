#22.10.24
#부등호
#실버1
#백트래킹

#순열 - 시간초과
#모든 경우의 수를 확인하므로 시간초과가 발생한다.
from itertools import permutations

k = int(input())
marks = list(input().rstrip().split())
lst = [str(n) for n in range(10)]
answer = []

for case in permutations(lst, k+1):
  for i in range(k):
    if not eval(case[i]+marks[i]+case[i+1]):
      break
  else:
    answer.append("".join(case))

answer.sort()

print(answer[-1])
print(answer[0])

#백트래킹
#브루트 포스를 적용하나 부등호 체크를 통해 백트래킹하여 시간을 단축한다.
k = int(input())
marks = list(input().rstrip().split())
visited = [False] * 10
max_n, min_n = "", ""

def back(lst):
  global min_n, max_n
  if len(lst) == k+1:
    if min_n == "":
      min_n = "".join(lst)
    else:
      max_n = "".join(lst)
    return

  for i in range(10):
    if len(lst) == 0:
      visited[i] = True
      back([str(i)])
      visited[i] = False
    elif visited[i] == False:
      if eval(lst[-1]+marks[len(lst)-1]+str(i)):
        visited[i] = True
        back(lst+[str(i)])
        visited[i] = False

back([])
print(max_n)
print(min_n)
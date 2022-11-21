#22.11.21
#n과 m(12)
#class4/실버2
#백트래킹

#백트래킹
import sys
sys.setrecursionlimit(10**4)

def bt(cur):
  if len(answer) == m:
    print(*answer)
    return
  
  overlap = 0
  for i in range(cur, n):
    if overlap != lst[i]:
      answer.append(lst[i])
      overlap = lst[i]
      bt(i)
      answer.pop()

n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
answer = []

bt(0)

#백트래킹 다른 풀이
def bt(cur):
  if len(answer) == m:
    print(*answer)
    return
  
  for i in range(cur, l):
    answer.append(lst[i])
    bt(i)
    answer.pop()

n, m = map(int, input().split())
lst = list(set(map(int, input().split())))
lst.sort()
l = len(lst)
answer = []

bt(0)

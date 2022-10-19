#22.10.18
#회의실 배정
#class3/실버1

#dp 적용(비효율)
#입력의 최대 숫자가 2^31-1 >= 20억이므로 모든 원소를 가진 리스트를 만드는 것은 시간 내로 불가능하다.
import sys
from collections import defaultdict

N = int(sys.stdin.readline())
dic = defaultdict(list)

for _ in range(N):
  s, e = map(int, sys.stdin.readline().split())
  dic[e].append(s)

for k in dic.keys():
  dic[k].sort()

answer = [0 for _ in range(max(dic.keys())+1)]

for i in range(len(answer)):
  for j in dic[i]:
    if i == j:
      if i == 0:
        answer[i] += 1
      else:
        answer[i] = max(answer[i]+1, answer[i-1]+1)
    else:
      answer[i] = max(answer[j]+1, answer[i])
  if i != 0:
    answer[i] = max(answer[i], answer[i-1])
    
print(answer[-1])

#그리디 적용
import sys

N = int(sys.stdin.readline())
lst = []

for _ in range(N):
  lst.append(list(map(int, sys.stdin.readline().split())))

end = [0]
lst.sort(key = lambda x: (x[1], x[0]))

for tmp in lst:
  if tmp[0] >= end[-1]:
    end.append(tmp[1])

print(len(end)-1)
#21.08.09
import sys
lst = []
for i in range(5):
  lst.append(sys.stdin.readline().rstrip())
# 가장 긴 요소의 길이값만큼 첫 번째 반복문이 진행된다.
for i in range(max([len(e) for e in lst])):
  for j in range(5):
    if i < len(lst[j]):
      print(lst[j][i], end='')
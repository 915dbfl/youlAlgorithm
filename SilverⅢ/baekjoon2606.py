#21.10.08
def countPair(index):
  global pairs, check
  if index in pairs:
    for i in pairs[index]:
      if i not in check:
        check.add(i)
        countPair(i)
  
import sys
n = int(input())
pnum = int(input())
pairs = {}
check = set()
check.add(1)
for i in range(1, n+1):
  pairs[i] = []

for i in range(pnum):
  str, end = map(int, sys.stdin.readline().rstrip().split())
  pairs[str].append(end)
  pairs[end].append(str)

countPair(1)
print(len(check)-1)
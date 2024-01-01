#22.09.13
#누울 자리를 찾아라

# 이중 for문 사용
def getSpot(states):
  count = 0
  spot = 0
  for row in states:
    for col in row:
      if col == ".":
        count += 1
      else:
        if count >= 2:
          spot += 1
        count = 0
    if count >= 2:
      spot += 1
    count = 0
  return spot

n = int(input())
state = []

for i in range(n):
  state.append(input())

print(getSpot(state), getSpot(zip(*state)))

# 정규식 사용
import re

def getSpot(states):
  count = 0
  for row in states:
    lst = re.findall('[.]{2,}', row)
    count += len(lst)
  return count

n = int(input())
state = []

for i in range(n):
  state.append(input())

tmp = map(''.join, zip(*state))

print(getSpot(state), getSpot(tmp))
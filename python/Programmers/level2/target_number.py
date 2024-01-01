#2022.03.13
#타켓 넘버

# 내 풀이
def solution(numbers, target):
  answer = 0
  lsts = [[]]
  for i in numbers:
    for j in range(len(lsts)):
      tmp = [k for k in lsts[j]]
      lsts[j].append(i)
      tmp.append(-i)
      lsts.append(tmp)

  for lst in lsts:
    if sum(lst) == target:
      answer += 1

  return 1

# 깊이 우선 탐색 (BEST)
def solution(numbers, target):
  if not numbers and target == 0:
    return 1
  elif not numbers:
    return 0
  else:
    return solution(numbers[1:], target - numbers[0]) + solution(numbers[1:], target + numbers[0])

# product 사용
from itertools import product

def solution(numbers, target):
  lst = [[i, -i] for i in numbers]
  tmp = list(map(sum, product(*lst)))
  return tmp.count(target)
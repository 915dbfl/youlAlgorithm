#2022.02.27
#소수 만들기

import itertools

def solution(nums):
  answer = 0

  for a in itertools.combinations(nums, 3):
    b = sum(a)
    for i in range(2, b):
      if b % i == 0:
        break
    else: # for문을 다 돌고 빠져나왔을 경우만 실행됨
      answer += 1

  return answer
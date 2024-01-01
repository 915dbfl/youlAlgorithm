#2022.03.10
#124 나라의 숫자

#나의 풀이
def solution(n):
  rule = {1: '1', 2: '2', 0: '4'}
  answer = ''
  
  while n != 0:
    answer += rule[n%3]
    if n % 3 == 0:
      n = (n // 3) -1
    else:
      n //= 3

  return answer[::-1]

#best 풀이
def solution(n):
  rule = ['1', '2', '4']
  answer = ''

  while n != 0:
    n -= 1
    answer = rule[n%3] + answer
    n //= 3

  return answer
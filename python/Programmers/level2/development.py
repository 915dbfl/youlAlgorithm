#2022.03.11
#기능개발

#내 풀이 
from math import ceil
from turtle import speed

def solution(progresses, speeds):
  answer = []
  dates = list(map(lambda x: ceil((100-progresses[x])/speeds[x]), range(len(progresses))))

  cnt = 1
  for i in range(1, len(progresses)):
    if dates[i-1] >= dates[i]:
      dates[i] = dates[i-1]
      cnt += 1
    else:
      answer.append(cnt)
      cnt = 1
        
  answer.append(cnt)
  return answer

#best 풀이
def solution(progresses, speeds):
  q = []
  
  #올림을 사용하는 대신에 음수에서의 //을 사용해 이를 다시 양수로 바꿈으로써 올림의 효과를 내고 있다.
  for p, s in zip(progresses, speeds):
    if len(q) == 0 or q[-1][0] < -((p-100)//s):
      q.append([-((p-100)/s), 1])
    else:
      q[-1][1] += 1

  return [i[1] for i in q]
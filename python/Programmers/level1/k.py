#2022.03.04
#k번재 수

def solution(array, commands):
  answer = []

  for i, j, k in commands:
    lst = array[i-1: j]
    lst.sort()
    answer.append(lst[k-1])

  return answer

  #return list(map(lambda x: sorted(array[x[0]-1: x[1]])[x[2] - 1]))
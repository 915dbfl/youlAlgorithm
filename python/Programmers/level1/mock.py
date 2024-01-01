#2022.03.04
#모의고사

def solution(answers):
  answer = []
  tmp = [0, 0, 0]
  students = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]

  for i in range(3):
    for j in range(len(answers)):
      k = j % len(students[i])
      if students[i][k] == answers[j]:
        tmp[i] += 1

  m = max(tmp)
  for i in range(3):
    if tmp[i] == m:
      answer.append(i+1)

  return answer

# enumerate(반복 가능한 객체)
# (index, 해당 index의 값)이 튜플 형태로 반환됨.
#23.01.16
#행렬 제곱
#골드 4

#O(b): 시간 초과
import sys

a, b = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(a)]
answer = [[0]*a for _ in range(a)]

for i in range(a):
  for j in range(a):
    answer[i][j] = matrix[i][j] % 1000

for _ in range(b-1):
  new = [[0]*a for _ in range(a)]
  for i in range(a):
    for j in range(a):
      for k in range(a):
        new[i][j] += (answer[i][k] * matrix[k][j])%1000
  answer = new

for m in answer:
  for n in m:
    print(n%1000, end = " ")
  print()

# 빠른 제곱 알고리즘
# 거듭제곱 분할정복 적용하기
import sys

def mul(m1, m2):
  new = [[0]*a for _ in range(a)]
  for i in range(a):
    for j in range(a):
      for k in range(a):
        new[i][j] += (m1[i][k] * m2[k][j])%1000
      new[i][j] %= 1000

  return new

def getMatrix(time):
  if time == 1:
    return matrix

  else:
    tmp = getMatrix(time//2)
    result = mul(tmp, tmp)
    if time % 2 == 0:
      return result
    else:
      return mul(result, matrix)

a, b = map(int, sys.stdin.readline().split())
matrix = [list(map(lambda x: int(x)%1000, sys.stdin.readline().split())) for _ in range(a)]

for m in getMatrix(b):
  print(*m)
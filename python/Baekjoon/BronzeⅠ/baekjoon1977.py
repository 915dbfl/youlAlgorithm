# #21.08.06
import math
m = int(input())
n = int(input())
lst = []
# 범위 시작과 끝 수의 루트값을 계산해 범위 내 제곱수 값 구하기
for i in range(math.ceil(m**0.5), int(n**0.5) + 1):
  lst.append(i**2)
if len(lst) == 0:
  print(-1)
else:
  #포매팅을 통해 두 값 출력
  print(f'{sum(lst)}\n{lst[0]}')
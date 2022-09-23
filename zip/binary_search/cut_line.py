#22.09.23
#랜선 자르기
#이분 탐색
#class2_1

import sys

K, N = map(int, sys.stdin.readline().split())
lst = []

for i in range(K):
  lst.append(int(sys.stdin.readline()))

e = sum(lst)//N
s = max(1, max(lst)//N)

while s <= e:
  mid = (e+s)//2

  if N <= sum(list(map(lambda x: x//mid, lst))):
    s = mid + 1
  else:
    e = mid - 1
  
print((e+s)//2)

# 이분 탐색 시작을 0으로 설정할 경우, 0으로 수렴하는 형태가 되어 ZerorDivisionError가 발생할 수 있다.
# 따라서 이분 탐색 시작은 적어도 1이어야 한다.
from copy import deepcopy
def c_front(n, k, order):
  # 입력: n, k
  # 출력: 동전을 던졌을 때, 앞면이 나온 횟수가 k인 경우/ 0(뒷면), 1(앞면)
  temp = deepcopy(order)
  if len(order) == n and order.count(1) == k:
    print(order)
  elif order.count(0) <= n-k:
    if order.count(1) <= k:
      temp.append(1)
      c_front(n, k, temp)
      temp.pop()
      temp.append(0)
      c_front(n, k, temp)

lst = []
c_front(3, 2, lst)
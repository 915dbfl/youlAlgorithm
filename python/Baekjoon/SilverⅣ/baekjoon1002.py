#21.09.05
n = int(input())
for i in range(n):
  x1, y1, r1, x2, y2, r2 = list(map(int, input().split()))
  l = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
  r = [r1, r2, l]
  m = max(r)
  r.remove(m)

  # 중심이 동일하고 반지름까지 같을 경우
  if (l == 0 and r1 == r2):
    print(-1)
  # 외접이거나 내접일 경우
  elif (l == r1 + r2 or m ==sum(r)):
    print(1)
  # 한 원 내부에 다른 원이 닿지 않고 존재하거나, 두 원이 완전히 다른 위치에 있어 겹치지 않는 경우
  elif (m > sum(r)):
    print(0)
  # 두 원이 두 점에서 만나는 경우
  else:
    print(2)
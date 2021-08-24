# 21.08.24
E, S, M = map(int, input().split())
year = E
while True:
  if (year - S) % 28 == 0 and (year - M) % 19 == 0:
    print(year)
    break
  year += 15
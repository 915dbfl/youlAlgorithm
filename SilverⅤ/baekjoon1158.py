#21.08.20
n, k = map(int,input().split())
lst = [str(i) for i in range(1, n+1)]
permu = []
turn = k - 1
for i in range(n):
  permu.append(lst[turn])
  del(lst[turn])
  if i != n-1:
    turn = (turn + (k-1)) % len(lst)
print('<' + ', '.join(permu) + '>')
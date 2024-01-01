#21.09.22
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
S = 0
for i in range(len(B)):
  b_max = max(B)
  A_min = min(A)
  S += b_max*A_min
  B.remove(b_max)
  A.remove(A_min)
print(S)
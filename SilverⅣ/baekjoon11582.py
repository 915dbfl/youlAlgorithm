#21.09.24
#분할정복
def sorting(start, end, k):
  global A, N
  range = N // k
  if (end - start + 1) != range:
    mid = start + (end - start + 1)//2
    sorting(start, mid-1, k)
    sorting(mid, end, k)
  else:
    B = sorted(A[start:end+1])
    for i in B:
      print(i, end=" ")

N = int(input())
A = list(map(int, input().split()))
K = int(input())
sorting(0, N-1, K)

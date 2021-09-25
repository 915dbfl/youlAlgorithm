#21.09.25
N, R = map(int, input().split())
lst = [i for i in range(1, N+1)]
p_index = R-1
print("<", end = "")
for i in range(N):
  if len(lst) == 1:
    print(lst.pop(), end="")
    print(">")
    break
  else:
    print(lst.pop(p_index), end=", ")
    p_index = (p_index + R - 1) % len(lst)
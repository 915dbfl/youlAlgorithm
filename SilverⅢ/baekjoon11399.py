#21.10.04
N = int(input())
time = list(map(int, input().split()))
time.sort()
delay = 0
i = N-1
for j in range(1, N+1):
  delay += time[i] * j
  i -= 1
print(delay)
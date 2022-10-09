#22.10.09
#z
#class3/실버1

n, r, c = map(int, input().split())

answer = 0

while n > 0:
  answer += (r//2**(n-1))*(2**(n-1)*2**(n-1)*2)
  answer += (c//2**(n-1))*2**(n-1)*2**(n-1)

  r -= (r//2**(n-1))*2**(n-1)
  c -= (c//2**(n-1))*2**(n-1)
  
  n -= 1
print(answer)
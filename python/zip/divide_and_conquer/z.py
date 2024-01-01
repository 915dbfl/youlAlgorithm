#22.10.09
#z
#class3/실버1
#분할 정복/재귀

#내 풀이: 분할정복
n, r, c = map(int, input().split())

answer = 0

while n > 0:
  answer += (r//2**(n-1))*(2**(n-1)*2**(n-1)*2)
  answer += (c//2**(n-1))*2**(n-1)*2**(n-1)

  r -= (r//2**(n-1))*2**(n-1)
  c -= (c//2**(n-1))*2**(n-1)
  
  n -= 1
print(answer)

#분할정복-1
n, r, c = map(int, input().split())

answer = 0

while n > 0:
  if r < 2**(n-1) and c < 2**(n-1): #1사분면
    answer += 2**(n-1) * 2**(n-1) * 0
  elif r < 2**(n-1) and c >= 2**(n-1): #2사분면
    answer += 2**(n-1) * 2**(n-1) * 1
    c -= 2**(n-1)
  elif r >= 2**(n-1) and c < 2**(n-1):#3사분면
    answer += 2**(n-1) * 2**(n-1) * 2
    r -= 2**(n-1)
  elif r >= 2**(n-1) and c >= 2**(n-1):
    answer += 2**(n-1) * 2**(n-1) * 3
    r -= 2**(n-1)
    c -= 2**(n-1)

  n -= 1

print(answer)

#재귀
def getAnswer(N, r, c):
  if N == 0:
    return 0
  return 2*(r%2)+(c%2) + 4 * getAnswer(N-1, r//2, c//2)

n, r, c = map(int, input().split())

print(getAnswer(n, r, c))
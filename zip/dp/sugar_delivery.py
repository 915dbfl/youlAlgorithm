#22.09.28
#설탕 배달
#class2/silver4
#탐욕(Greedy)/DP(동적계획법)
#Greedy: 미래를 고려하지 않고 지금 고르는 선택이 가장 최선이기 바라는 기법/단, 주어진 조건에 따라 항상 최선의 결과가 나온다는 보장 없음.

#내 풀이(그리디)
N = int(input())

five = N//5

for i in range(five, -1, -1):
  three = (N-(i*5))%3
  if three == 0:
    print(i+((N-(i*5))//3))
    break
else:
  print(-1)

#다른 풀이(그리디)
N = int(input())
cnt = 0

while 1:
  if N % 5 != 0:
    cnt += 1
    N -= 3
  elif N % 5 == 0:
    print(cnt + N//5)
    break
  
  if N < 0:
    print(-1)
    break

# 동적계획법
N = int(input())
lst = [-1 for _ in range(N+1)]

if N >= 3:
  lst[3] = 1
if N >= 5:
  lst[5] = 1

for i in range(6, N+1):
  if lst[i-5] == -1 and lst[i-3] == -1:
    continue
  elif lst[i-5] == -1:
    lst[i] = lst[i-3] +1
  elif lst[i-3] == -1:
    lst[i] = lst[i-5] +1
  else:
    lst[i] = min(lst[i-5], lst[i-3]) +1

print(lst[N])
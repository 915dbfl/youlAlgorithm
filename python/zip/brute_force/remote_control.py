# #22.10.10
# #리모컨
# #class3/골드5
# #브루트 포스

n = int(input())
c = int(input())

if c > 0:
  s = set(input().rstrip().split())
else:
  s = set()

move = abs(100-n)

if c == 10:
  print(move)
elif c == 0:
  print(min(move, len(str(n))))
else:
  cnt = [0, 0]
  while 1: # n보다 작은 수 중 최댓값
    tmp1 = set(str(n-cnt[0]))
    
    if len(tmp1 & s) == 0:
      move = min(move, cnt[0]+len(str(n-cnt[0])))
      break

    cnt[0] += 1
  
  while 1: # n보다 큰 수 중 최솟값
    if cnt[1] > cnt[0]:
      break
    tmp2 = set(str(n+cnt[1]))

    if len(tmp2 & s) == 0:
      move = min(move, cnt[1]+len(str(n+cnt[1])))
      break
    
    cnt[1] += 1

  print(move)

# 브루트 포스 최적화
import sys
input = sys.stdin.readline

n = int(input())
min_count = abs(100-n)

c = int(input())
if c > 0:
  broken = list(map(int, input().split()))
else:
  broken = []

for nums in range(1000001):
  nums = str(nums)

  for j in range(len(nums)):
    if int(nums[j]) in broken:
      break
    elif j == len(nums)-1:
      min_count = min(min_count, len(nums)+ abs(int(nums)-n))

print(min_count)
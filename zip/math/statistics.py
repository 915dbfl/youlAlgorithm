#22.09.25
#통계학
#class2_1
#정렬, 반올림, 최빈값

from collections import Counter
import sys

N = int(sys.stdin.readline())
nums = []

for _ in range(N):
  nums.append(int(sys.stdin.readline()))

nums.sort()
print(int(round(sum(nums)/N)))
print(nums[N//2])

tmp = Counter(nums).most_common(2)
if len(tmp) == 1:
  print(tmp[0][0])
elif tmp[0][1] == tmp[1][1]:
  print(max(tmp[0][0], tmp[1][0]))
else:
  print(tmp[0][0])
print(nums[-1]-nums[0])

#collections 모듈 속 Counter
#Counter(a): a 속 요소마다 개수가 딕셔너리 형태로 주어진다.
#Counter(a).most_common(n): a 속 요소 중 최빈값 n개를 반환한다. 이때 리스트에 담긴 튜플형태로 반환!!!

#math모듈
#math.ceil(올림)
#math.floor(내림)
#math.trunc(버림)

#round(a, n): a를 소수점 n자리까지 반올림해서 나타냄
#여기서 주의할 점은 a가 올림, 내림했을 떄 동일하게 차이나는 경우(0.5, 2.5, 6.5..) 짝수 값으로 반올림!(0, 2, 6)
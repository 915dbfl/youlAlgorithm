#22.10.03
#숫자 카드2
#class2/실버4
#Counter/해시
#이분탐색: nums 값을 받아와 오름차순 정렬한 후, 찾고자 하는 값과 중간값을 비교하며 범위를 줄여나간다.
  # 해당 범위에서 찾고자 하는 값을 count를 통해서 찾는다.

from collections import Counter

n1 = int(input())

nums = Counter(map(int, input().split()))

n2 = int(input())

for i in list(map(int, input().split())):
  print(nums[i], end = " ")
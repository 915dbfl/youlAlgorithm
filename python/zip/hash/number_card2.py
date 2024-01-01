#22.10.03
#숫자 카드2
#class2/실버4
#Counter/해시
#이분탐색: nums 값을 받아와 오름차순 정렬한 후, 찾고자 하는 값과 중간값을 비교하며 범위를 줄여나간다.
  # 해당 범위에서 찾고자 하는 값을 count를 통해서 찾는다.

# Counter 풀이
from collections import Counter

n1 = int(input())

nums = Counter(map(int, input().split()))

n2 = int(input())

for i in list(map(int, input().split())):
  print(nums[i], end = " ")

#이분탐색 풀이(시간초과)
n1 = int(input())

nums1 = sorted(list(map(int, input().split())))

n2 = int(input())
nums2 = list(map(int, input().split()))

for n in nums2:
  s = 0
  e = n1-1
  while s <= e:
    mid = (s+e)//2
    if nums1[mid] > n:
      e = mid-1
    elif nums1[mid] < n:
      s = mid+1
    else:
      break
  
  print(nums1[s:e+1].count(n), end = " ")

# 이진탐색 모듈 사용하기: bisect

from bisect import bisect_left, bisect_right

def count_by_range(nums, num):
  r_i = bisect_right(nums, num)
  l_i = bisect_left(nums, num)
  return r_i - l_i

n1 = int(input())
nums1 = sorted(list(map(int, input().split())))

n2 = int(input())
nums2 = list(map(int, input().split()))

for i in nums2:
  print(count_by_range(nums1, i), end = " ")
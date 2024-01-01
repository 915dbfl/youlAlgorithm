#22.11.08
#좌표 압축
#class3/실버2
#정렬/해시

from collections import defaultdict

n = int(input())
lst = list(map(int, input().split()))
nums = sorted(list(set(lst)))
dic = defaultdict(int)

for idx, val in enumerate(nums):
  dic[val] = idx

for i in lst: # 해시값을 통해 값을 가져오는 작업은 O(1)
  print(dic[i], end = " ")
#23.01.10
#숫자 카드
#알고리즘 4주차-1
#실버4

# #list에서 in 시간복잡도: O(n)
# #set에서 in 시간복잡도: O(1)
import sys
input = sys.stdin.readline

n = int(input())
lst = set(map(int, input().split()))

m = int(input())
for i in list(map(int, input().split())):
  if i in lst:
    print(1, end = " ")
  else:
    print(0, end = " ")

#이분 탐색
import sys
input = sys.stdin.readline

def binary_search(i):
  start = 0
  end = n-1

  while start <= end:
    mid = (start+end)//2

    if lst[mid] == i:
      return True
    elif lst[mid] < i:
      start = mid+1
    else:
      end = mid-1
  return False

n = int(input())
lst = list(map(int, input().split()))
lst.sort()

m = int(input())
for i in list(map(int, input().split())):
  if binary_search(i):
    print(1, end = " ")
  else:
    print(0, end = " ")
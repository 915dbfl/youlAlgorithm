# n <= 100,000
# 새로운 값이 들어올 때마다 정렬 해야 함 -> 이진탐색으로 정렬 진행 O(logN)

# 이진탐색 시간복잡도 초과
def getNewBase(target, base):
    # 이진 탐색으로 target이 들어갈 위치 탐색
    start = 0
    end = len(base) - 1

    while start <= end:
        mid = (start + end) // 2
        
        if base[mid] <= target:
            start = mid + 1
        else:
            end = mid - 1

    # target을 포함하는 새로운 배열 생성 후 반환
    # ⛔️ 이 부분에서 시간 복잡도 O(n)
    if end < 0:
        newBase = [target] + base
    else:
        newBase = base[:end+1] + [target] + base[end+1:]
    
    return newBase

n = int(input())
base = [int(input())]
print(base[0])

for _ in range(n-1):
    num = int(input())
    base = getNewBase(num, base)
    
    # 짝수 개라면
    print(base[(len(base)-1)//2])

# 힙 사용하기
# 최소/최대 힙 사용하기
import sys
input = sys.stdin.readline
from heapq import heappop, heappush

n = int(input())
left = [] # 중간값을 포함한 이전 값 최대힙
right = [] # 중간값 이후 값 최소힙

for _ in range(n):
    x = int(input())

    # left가 비어있거나
    # 현재 입력값이 left에서 제일 작은 값보다 작거나 같으면
    if len(left) == 0 and -left[0] >= x:
        heappush(left, -x)
    else:
        heappush(right, x)

    # left가 right에 1을 더한 것보다 더 길면
    if len(left) > len(right) + 1:
        # left에서 제일 큰 값을 빼서 right에 넣는다.(바로 정렬이 됨)
        temp = -heappop(left)
        heappush(right, temp)
    # right가 left보다 길면
    elif len(right) > len(left):
        # right에서 제일 작은 값을 빼서 left에 넣는다.(바로 정렬이 됨)
        temp = heappop(right)
        heappush(left, -temp)

    print(-left[0])
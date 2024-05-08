import sys
from collections import defaultdict
input = sys.stdin.readline

# 이분탐색, 투포인터 -> 50점
def is_Possible(pack_size):
    visited = defaultdict(int)
    cnt = 0
    left = 0

    # 투포인터 진행 -> 최악의 경우 O(n**2)
    for right in range(n+1):
        visited[cards[right]] += 1
        # 이미 다른 슬라이딩 윈도에 포함되었다면 left 증가
        while visited[cards[right]] > 1:
            visited[cards[left]] -= 1
            left += 1
        # pack_size일 경우에만 count
        if right - left + 1 == pack_size:
            cnt += 1
            # 해당 범위 슬라이딩 윈도우에서 제외
            while left != right:
                visited[cards[left]] -= 1
                left += 1

    if cnt >= m:
        return True
    return False

n, m = map(int, input().split())
cards = list(map(int, input().split()))
cards.append(cards[-1])

left = 1
right = n
answer = 0

# 이분탐색으로 가능한 pack_size 확인
while left <= right:
    mid = (left + right)//2
    if is_Possible(mid):
        left = mid + 1
        answer = mid
    else:
        right = mid - 1
print(answer)

# 다시 탐색해야 하는 지점 저장해 활용
import sys
input = sys.stdin.readline

def is_Possible(size):
    cnt = 0
    cur = 0
    
    # 범위를 넘어가지 않는 경우만 확인
    while cur + size <= n:
        visited = dict()
        for i in range(cur, cur + size):
            # 처음 방문하는 카드라면
            if cards[i] not in visited:
                visited[cards[i]] = i
            # 기존에 방문했던 카드라면
            else:
                cur = visited[cards[i]] + 1
                break
        # 성공한 경우만
        else:
            cnt += 1
            cur = cur + size
            
    if cnt >= m:
        return True
    else:
        return False

n, m = map(int, input().split())
cards = list(map(int, input().split()))

left = 1
right = n
answer = 0
while left <= right:
    mid = (left + right)//2
    if is_Possible(mid):
        answer = mid
        left = mid + 1
    else:
        right = mid - 1
print(answer)
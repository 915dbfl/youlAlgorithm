# 우선 순위 큐 - 동기화 문제

# dictionary를 이용한 풀이
import sys
from heapq import heappop, heappush
from collections import defaultdict

t = int(input())
for _ in range(t):
    minhq = []
    maxhq = []
    nums = defaultdict(int)
    k = int(input())
    cnt = 0

    for _ in range(k):
        ord, n = sys.stdin.readline().split()
        n = int(n)

        if ord == "I":
            nums[n] += 1
            heappush(minhq, n)
            heappush(maxhq, -n)
            cnt += 1
        else:
            if cnt > 0:
                if n == 1:
                    while nums[-maxhq[0]] == 0:
                        heappop(maxhq)
                    nums[-maxhq[0]] -= 1
                    cnt -= 1
                    heappop(maxhq)
                else:
                    while nums[minhq[0]] == 0:
                        heappop(minhq)
                    nums[minhq[0]] -= 1
                    cnt -= 1
                    heappop(minhq)

    if cnt <= 0:
        print("EMPTY")
    else:
        while nums[minhq[0]] == 0:
            heappop(minhq)
        while nums[-maxhq[0]] == 0:
            heappop(maxhq)
        print(-maxhq[0], minhq[0])

# 다른 풀이
# 두 힙의 동기화를 위해 visited를 사용하자.
import sys
from heapq import heappop, heappush

t = int(input())
for _ in range(t):
    minhq = []
    maxhq = []
    visited = [False] * 1000001
    k = int(input())

    for key in range(k):
        ord, n = input().split()
        n = int(n)
        if ord == "I":
            heappush(maxhq, (-n, key))
            heappush(minhq, (n, key))
            visited[key] = True
        else:
            if n == -1:
                while minhq and not visited[minhq[0][1]]:
                    heappop(minhq)
                if minhq:
                    visited[minhq[0][1]] = False
                    heappop(minhq)
            else:
                while maxhq and not visited[maxhq[0][1]]:
                    heappop(maxhq)
                if maxhq:
                    visited[maxhq[0][1]] = False
                    heappop(maxhq)

    while maxhq and not visited[maxhq[0][1]]:
        heappop(maxhq)
    while minhq and not visited[minhq[0][1]]:
        heappop(minhq)

    if minhq and maxhq:
        print(-maxhq[0][0], minhq[0][0])
    else:
        print("EMPTY")
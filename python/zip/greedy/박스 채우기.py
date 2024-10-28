# 오답,,
import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

l, w, h = map(int, input().split())
types = defaultdict(int)
n = int(input())

for _ in range(n):
    powCnt, amount = map(int, input().split())
    types[2**powCnt] = amount

def fillRectangle(x, y, length, width, height):
    global n
    answer = sys.maxsize
    if length == 0 or width == 0 or height == 0: return 0

    for i in range(n-1, -1, -1):
        type = 2**i

        if types[type] <= 0: continue

        # 박스 안에 들어갈 수 있는 정육면체인지 확인
        if length >= type and width >= type and height >= type:
            cnt = min(height // type, types[type])
            types[type] -= cnt
            bottom = fillRectangle(x+type, y, length, width - type, type * cnt)
            right = fillRectangle(x+type, y+type, length - type, type, type * cnt)
            top = fillRectangle(x, y, length, width, height - (type * cnt))
        
            answer = min(answer, cnt + bottom + right + top)
    
    return answer

result = fillRectangle(0, 0, l, w, h)
print(-1 if result == sys.maxsize else result)

# 그리디 알고리즘
length, width, height = map(int, input().split())
n = int(input())
cube = [list(map(int, input().split())) for _ in range(n)]
volume = length * width * height
ans = 0
before = 0
cube.sort(reverse=True)

for w, cnt in cube:
    before <<= 3
    v = 2 ** w
    maxCnt = (length // v) * (width // v) * (height // v) - before
    maxCnt = min(cnt, maxCnt)
    ans += maxCnt
    before += maxCnt

if before == volume:
    print(ans)
else:
    print(-1)
import sys
input = sys.stdin.readline
INF = sys.maxsize

n = int(input())

yearH = []
yearT = []
for _ in range(n):
    u, v = map(int, input().split())
    yearH.append(u)
    yearT.append(v)

# 배열 마지막에 존재하는 늙은 날을 바탕으로 가능한 최대 젊은 날을 구하자
pointer_y = 0
pointer_o = n-1
while 1:
    checkH = yearH[pointer_y] == 0 or yearH[pointer_o] == 0 or (yearH[pointer_y] > yearH[pointer_o])
    checkT = yearT[pointer_y] == 0 or yearT[pointer_o] == 0 or (yearT[pointer_y] < yearT[pointer_o])

    if checkH and checkT:
        if pointer_y + 1 <= pointer_o:
            pointer_y += 1
        else:
            break
    else:
        break

# 늙은 날 최대 행복도 구하기
oldH_max = max(yearH[pointer_y:])
# 늙은 날 최소 피로도 구하기, 0이 존재하므로 직접 for문 도림
oldT_min = INF
for i in range(pointer_y, n):
    if yearT[i] != 0:
        oldT_min = min(yearT[i], oldT_min)

# 최종 젊은 날 구하기!
for i in range(pointer_y):
    if (yearH[i] != 0 and yearH[i] <= oldH_max) or (yearT[i] != 0 and yearT[i] >= oldT_min):
        pointer_y = i
        break

print(pointer_y if pointer_y != 0 else -1)

# 누적합 활용
# 젊은날 최소 행복도, 젊은날 최대 피로도
# 늙은날 최대 행복도, 늙은날 최소 피로도

import sys
input = sys.stdin.readline
INF = sys.maxsize

n = int(input())

yearH = []
yearT = []
for _ in range(n):
    u, v = map(int, input().split())
    yearH.append(u)
    yearT.append(v)

minH_y = [INF] * n
minH_y[0] = yearH[0] if yearH[0] != 0 else INF
maxT_y = [0] * n
maxT_y[0] = yearT[0] 

maxH_o = [0] * n
maxH_o[-1] = yearH[-1]
minT_o = [INF] * n
minT_o[-1] = yearT[-1] if yearT[-1] != 0 else INF

# 젊은날 최소 행복도, 최대 피로도 구하기
for i in range(1, n):
    if yearH[i] == 0: # 누락된 값일 경우 이전 최소 행복값 유지
        minH_y[i] = minH_y[i-1]
    else:
        minH_y[i] = min(yearH[i], minH_y[i-1])

    if yearT[i] == 0: # 누락된 값일 경우 이전 최대 피로도 유지
        maxT_y[i] = maxT_y[i-1]
    else:
        maxT_y[i] = max(yearT[i], maxT_y[i-1])

# 늙은날 최대 행복도, 최소 피로도 구하기
for i in range(n-2, -1, -1):
    if yearH[i] == 0: # 누락된 값일 경우 이전 최소 행복값 유지
        maxH_o[i] = maxH_o[i+1]
    else:
        maxH_o[i] = max(yearH[i], maxH_o[i+1])

    if yearT[i] == 0: # 누락된 값일 경우 이전 최대 피로도 유지
        minT_o[i] = minT_o[i+1]
    else:
        minT_o[i] = min(yearT[i], minT_o[i+1])

# 가능한 최대 젊은 날을 구하는 것이므로 n-1까지 for문을 돌며 확인
answer = 0
for i in range(n-1):
    if minH_y[i] > maxH_o[i+1] and maxT_y[i] < minT_o[i+1]:
        answer = i+1

print(answer if answer != 0 else -1)
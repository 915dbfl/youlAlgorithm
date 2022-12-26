#22.12.24
#사탕 게임
#알고리즘 스터디 1주차 -2

import sys
input = sys.stdin.readline

n = int(input())

lst = [list(input().rstrip()) for _ in range(n)]

def count(): # 숫자 교환 후 먹을 수 있는 최대 개수
  answer = 1
  for i in range(n): 
    cnt = 1
    for j in range(n-1): # 가로로 먹을 수 있는 최대 개수 구하기
      if lst[i][j] != lst[i][j+1]: # 같은 숫자가 아닐 경우
        cnt = 1
      else:
        cnt += 1
        if answer < cnt: answer = cnt

    cnt = 1
    for k in range(n-1): # 가로로 먹을 수 있는 최대 개수 구하기
      if lst[k][i] != lst[k+1][i]: # 같은 숫자가 아닐 경우
        cnt = 1
      else:
        cnt += 1
        if answer < cnt: answer = cnt
    
  return answer

answer = 1
# 중복을 제외하고 오른쪽/아래 방향으로 교환이 되는 모든 경우
for i in range(n):
  for j in range(n):
    if i < n-1:
      tmp = lst[i][j] # 교환
      lst[i][j] = lst[i+1][j]
      lst[i+1][j] = tmp

      answer = max(answer, count()) # 최대 개수 업데이트

      tmp = lst[i][j] # 교환 취소
      lst[i][j] = lst[i+1][j]
      lst[i+1][j] = tmp
    
    if j < n-1:
      tmp = lst[i][j] # 교환
      lst[i][j] = lst[i][j+1]
      lst[i][j+1] = tmp

      answer = max(answer, count()) # 최대 개수 업데이트
    
      tmp = lst[i][j] # 교환 취소
      lst[i][j] = lst[i][j+1]
      lst[i][j+1] = tmp

print(answer)
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
height = []
answer = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(n):
    height.append(list(map(int, input().split())))

# 0번째 라인 폭탄 개수 구하기
dif = m // 2
answer[dif][dif] = -height[0][0]
for i in range(1, n-m+1):
    answer[dif][i+dif] = -height[0][i] + height[0][i-1]
    if 0<=i - m:
        answer[dif][i+dif] += answer[dif][i-m+dif]

# i번째(i<0) 라인 폭탄 개수 구하기
for i in range(1, n-m+1):
    answer[dif+i][dif] = -height[i][0] + height[i-1][0]
    if 0<=i-3:
        answer[dif+i][dif] += answer[dif+i-3][dif]
    for j in range(1, n-m+1):
        answer[dif+i][dif+j] = -height[i][j] + height[i-1][j] + height[i][j-1] -height[i-1][j-1]
        if 0<=j-3:
            answer[dif+i][dif+j] += answer[dif+i][dif+j-3]
        if 0<=i-3:
            answer[dif+i][dif+j] += answer[dif+i-3][dif+j]
        if 0<=j-3 and 0<=i-3:
            answer[dif+i][dif+j] -= answer[dif+i-3][dif+j-3]

for i in range(n):
    print(" ".join(map(str, answer[i])))
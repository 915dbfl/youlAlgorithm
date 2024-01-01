#인간-컴퓨터 상호작용

# 문자열 2000자일 때 통과
import sys
str = input().rstrip()
n = int(input())

for _ in range(n):
    a, l, r = sys.stdin.readline().split()
    print(str[int(l):int(r)+1].count(a))


#누적합 100점 통과
import sys
from collections import defaultdict

str = input().rstrip()
n = int(input())
dic = defaultdict(list)

def createDic(a):
    dp = [0]* (len(str)+1)
    dp[1] = 1 if str[0] == a else 0

    for i in range(2, len(str)+1):
        if str[i-1] == a:
            dp[i] = dp[i-1] + 1
        else:
            dp[i] = dp[i-1]

    dic[a] = dp

for _ in range(n):
    a, l, r = sys.stdin.readline().split()
    if len(dic[a]) == 0:
        createDic(a)
        print(dic[a][int(r)+1] - dic[a][int(l)])
    else:
        print(dic[a][int(r)+1] - dic[a][int(l)])
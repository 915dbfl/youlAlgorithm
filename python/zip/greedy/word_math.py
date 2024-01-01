#23.01.04
#단어 수학
#알고리즘 스터디 3-3
#골드 4

#단순히 위치 = 우선순위로 생각한 경우
# 반례 (1772)
# 10
# ABB
# BC
# BC
# BC
# BC
# BC
# BC
# BC
# BC
# BC
import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
words = [input().rstrip() for _ in range(n)]

dic = defaultdict(list)
alpha_dic = defaultdict(int)

for word in words:
  l = len(word)

  for i, val in enumerate(word):
    dic[l-i].append(val)

val = 9
for i in range(max(dic.keys()), 0, -1):
  for j in dic[i]:
    if alpha_dic[j] == 0:
      alpha_dic[j] = str(val)
      val -= 1

answer = 0
for word in words:
  tmp = ""
  for i in word:
    tmp += alpha_dic[i]
  answer += int(tmp)
print(answer)

# 위치, 빈도에 따라 가중치를 고려한 경우
import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
words = []
weight = defaultdict(int)

for _ in range(n):
  word = input().rstrip()
  words.append(word)
  l = len(word)

  for i, val in enumerate(word):
    weight[val] += 10**(l-i-1)

alpha = defaultdict(int)
val = 9
for i in sorted(weight.keys(), key= lambda x: -weight[x]):
  alpha[i] = val
  val -= 1

# answer = 0
# for word in words:
#   tmp = ""
#   for i in word:
#     tmp += alpha[i]
#   answer += int(tmp)
# print(answer)

#리팩토링
answer = 0
for i in alpha.keys():
  answer += weight[i] * alpha[i]
print(answer)
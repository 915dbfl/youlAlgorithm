#2022.03.17
#메뉴 리뉴얼

#내 풀이 (combinations 사용)
from itertools import combinations as c

def getNewMenu(orders, course):
    dic = {}
    answer = []
    for i in orders:
        for j in c(i, course):
            j = tuple(sorted(j))  #튜플은 .sort()가 아닌 sorted()로 정렬하며 반환되는 것은 리스트이다.
            if j in dic.keys(): dic[j] += 1
            else: dic[j] = 1
    if len(dic) != 0:
        m = max(dic.values())
        if m >= 2:
            for i in dic.keys():
                if dic[i] == m:
                    answer.append("".join(i))
    return answer

def solution(orders, course):
    result = []
    for i in course:
        result += getNewMenu(orders, i)
    return sorted(result) #.sort()는 반환값이 없지만 sorted()는 정렬된 값을 반환한다.

# best 풀이(collections.Counter 사용)
import collections
import itertools

def solution(orders, course):
  result = []
  for i in course:
    course_combi = []
    for order in orders:
      course_combi += itertools.combinations(sorted(order), i) # 길이가 i인 모든 조합 얻기
    count_combi = collections.Counter(course_combi).most_common() # 가장 많이 존재한느 조합이 어느 것인지 파악
    result += ["".join(k) for k, v in count_combi if v >= 2 and v == count_combi[0][1]] # 등장 횟수가 가장 많은 조합들을 결과에 포함
  return sorted(result)
 
 # collections.Counter(대상)을 통해 대상 속 각 요소의 개수를 카운트한 딕셔너리를 얻는다.
 # most_common()을 통해 개수가 많은 순으로 정렬된 리스트를 얻는다. (각 요소는 '(요소, 개수)' 형태의 튜플)
#2022.03.20
#뉴스 클러스터링

#내 풀이
def solution(str1, str2):
    lst1 = []; lst2 = []
    count1 = 0; count2 = 0
    str1 = str1.upper()
    str2 = str2.upper()
    #1단계: 다중집합 원소 만들기
    for i in range(len(str1) -1):
        tmp = str1[i:i+2]
        if tmp[0].isalpha() and tmp[1].isalpha():
            lst1.append(tmp)
    for i in range(len(str2) -1):
        tmp = str2[i:i+2]
        if tmp[0].isalpha() and tmp[1].isalpha():
            lst2.append(tmp)

    #2단계: 교집합 구하기     
    lst3 = list(set(lst1) & set(lst2))
    for i in lst3:
        tmp1 = lst1.count(i)
        tmp2 = lst2.count(i)
        count1 += min(tmp1, tmp2)

    #3단계: 합집합 구하기        
    lst4 = list(set(lst1) | set(lst2))
    for i in lst4:
        tmp1 = lst1.count(i)
        tmp2 = lst2.count(i)
        count2 += max(tmp1, tmp2)

    if count2 == 0:
        return 65536
    return int((count1/count2) * 65536)

#best 풀이
import re

def solution(str1, str2):
    #1단계: 다중집합 원소 만들기
    lst1 = [str1[i:i+2].lower() for i in range(len(str1)-1) if not re.findall('[^a-zA-Z]+', str1[i:i+2])]
    lst2 = [str2[i:i+2].lower() for i in range(len(str2)-1) if not re.findall('[^a-zA-Z]+', str2[i:i+2])]
    
    inters = set(lst1) & set(lst2)
    aggreg = set(lst1) | set(lst2)
    
    if len(aggreg) == 0:
        return 65536
    
    #2-3단계: 교/합집합 만들기
    inters_sum = sum([min(lst1.count(i), lst2.count(i)) for i in inters])
    aggreg_sum = sum([max(lst1.count(i), lst2.count(i)) for i in aggreg])
    
    return int((inters_sum/aggreg_sum) * 65536)
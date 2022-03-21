#2022.03.20
#뉴스 클러스터링

#내 풀이
def solution(str1, str2):
    lst1 = []; lst2 = []
    count1 = 0; count2 = 0
    str1 = str1.upper()
    str2 = str2.upper()
    for i in range(len(str1) -1):
        tmp = str1[i:i+2]
        if tmp[0].isalpha() and tmp[1].isalpha():
            lst1.append(tmp)
    for i in range(len(str2) -1):
        tmp = str2[i:i+2]
        if tmp[0].isalpha() and tmp[1].isalpha():
            lst2.append(tmp)
            
    lst3 = list(set(lst1) & set(lst2))
    for i in lst3:
        tmp1 = lst1.count(i)
        tmp2 = lst2.count(i)
        count1 += min(tmp1, tmp2)
            
    lst4 = list(set(lst1) | set(lst2))
    for i in lst4:
        tmp1 = lst1.count(i)
        tmp2 = lst2.count(i)
        count2 += max(tmp1, tmp2)

    if count2 == 0:
        return 65536
    return int((count1/count2) * 65536)
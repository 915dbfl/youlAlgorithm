#22.09.18(해시)
#베스트앨범

# 장르 별 횟수를 판단해야 하므로 해시를 사용해야 한다.

# 내 풀이: 딕셔너리 두 개 사용
from collections import defaultdict

def solution(genres, plays):
    dic_album = defaultdict(list)
    dic_count = defaultdict(int)
    answer = []
    for i in range(len(genres)):
        dic_album[genres[i]].append(i)
        dic_count[genres[i]] += plays[i]
        
    order = sorted(list(dic_album.keys()), key = lambda x: dic_count[x], reverse = True)
    
    for i in order:
        answer += sorted(dic_album[i], key = lambda x: plays[x], reverse = True)[:2]
    
    return answer

# 다른 풀이: 딕셔너리 한 개 사용
from collections import defaultdict

def solution(genres, plays):
    genre = defaultdict(list)
    answer = []
    for i in range(len(genres)):
        genre[genres[i]].append([plays[i], i])
        
    order = sorted(list(genre.keys()), key = lambda x: sum(map(lambda y: y[0], genre[x])), reverse = True)
    
    for i in order:
        tmp = list(map(lambda y: y[1], sorted(genre[i], key = lambda x: (-x[0], x[1]))))
        answer += tmp[:min(len(tmp), 2)]
    
    return answer
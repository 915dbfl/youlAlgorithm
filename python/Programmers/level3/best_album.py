#22.07.19
#베스트 앨범

# 내 풀이
from collections import defaultdict
from functools import reduce

def solution(genres, plays):
    dic = defaultdict(list)
    for i in range(len(genres)):
        dic[genres[i]].append((i, plays[i]))

    groups = list(dic.values())
    for i in groups:
        i.sort(key = lambda x: (x[1], -x[0]), reverse = True)

    temp = []
    for i in groups:
        nums, amount = zip(*i)
        temp.append((nums[:2], sum(amount)))

    temp.sort(key = lambda x: x[1], reverse = True)
    nums, _ = zip(*temp)
    return reduce(lambda a, b: a+b, nums)

# class 활용
from collections import defaultdict

def solution(genres, plays):
    answer = []
    dic = defaultdict(int)
    album_list = defaultdict(list)
    for i in range(len(genres)):
        dic[genres[i]] += plays[i]
        album_list[genres[i]].append(album(genres[i], plays[i], i))
        
    dic = sorted(dic.items(), key = lambda x: x[1], reverse = True)
    
    answer = []
    for genre, _ in dic:
        album_list[genre].sort(reverse = True)
        for j in range(min(2, len(album_list[genre]))):
            answer.append(album_list[genre][j].track)
    return answer
    
class album:
    def __init__(self, genre, play, track):
        self.genre = genre
        self.play = play
        self.track = track

    # 아래 여섯 개의 스페셜 함수를 작성할 시, 클래스끼리 비교연산 가능!🔔    
    def __lt__(self, other):
        return self.play < other.play
    def __le__(self, other):
        return self.play <= other.play
    def __gt__(self, other):
        return self.play > other.play
    def __ge__(self, other):
        return self.play >= other.play
    def __eq__(self, other):
        return self.play == other.play
    def __ne__(self, other):
        return self.play != other.play

# 다른 좋은 풀이
from collections import defaultdict

def solution(genres, plays):
    answer = []
    dic = defaultdict(list)
    for e in zip(genres, plays, range(len(genres))):
        dic[e[0]].append([e[1], e[2]])
    
    # 각 장르마다 plays 총합을 구한 방식을 잘 살펴보자!🔔
    genreSort = sorted(dic.keys(), key = lambda x: sum(map(lambda y: y[0], dic[x])), reverse = True)
    
    for g in genreSort:
        temp = [e[1] for e in sorted(dic[g], key = lambda x: (x[0], -x[1]), reverse = True)]
        answer += temp[:2]
    return answer
        
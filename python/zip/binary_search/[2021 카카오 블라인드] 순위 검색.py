# 효율성 통과 못함..
from collections import defaultdict

class Participant:
    lans = ["python", "cpp", "java"]
    
    def __init__(self):
        self.dic = dict()
        for l in self.lans:
            self.dic[l] = Lan()
            
    def add_participant(self, lan, part, level, food, score):
        if lan == "-":
            for l in self.lans:    
                self.dic[l].add_participant(part, level, food, score)
        else:
            self.dic[lan].add_participant(part, level, food, score)
        
    def count_participant(self, lan, part, level, food, score):
        cnt = 0
        if lan == "-":
            for l in self.lans:
                cnt += self.dic[l].count_participant(part, level, food, score)
        else:
             cnt += self.dic[lan].count_participant(part, level, food, score)
                
        return cnt
        
class Lan:
    part = ["backend", "frontend"]

    def __init__(self):
        self.dic = dict()
        for p in self.part:
            self.dic[p] = Part()
            
    def add_participant(self, part, level, food, score):
        if part == "-":
            for p in self.part:
                self.dic[p].add_participant(level, food, score)
        else:
            self.dic[part].add_participant(level, food, score)
            
    def count_participant(self, part, level, food, score):
        cnt = 0
        if part == "-":
            for p in self.part:
                cnt += self.dic[p].count_participant(level, food, score)
        else:
            cnt += self.dic[part].count_participant(level, food, score)
    
        return cnt
                    
class Part:
    level = ["junior", "senior"]
    
    def __init__(self):
        self.dic = dict()
        for lv in self.level:
            self.dic[lv] = Level()
            
    def add_participant(self, level, food, score):
        if level == "-":
            for lv in self.level:
                self.dic[lv].add_participant(food, score)
        else:
            self.dic[level].add_participant(food, score)
            
    def count_participant(self, level, food, score):
        cnt = 0
        if level == "-":
            for lv in self.level:
                cnt += self.dic[lv].count_participant(food, score)
        else:
            cnt += self.dic[level].count_participant(food, score)
    
        return cnt

class Level:
    food = ["pizza", "chicken"]
    
    def __init__(self):
        self.dic = dict()
        for f in self.food:
            self.dic[f] = Food()
            
    def add_participant(self, food, score):
        if food == "-":
            for f in self.food:
                self.dic[f].add_participant(score)
        else:
            self.dic[food].add_score(score)
            
    def count_participant(self, food, score):
        cnt = 0
        if food == "-":
            for f in self.food:
                cnt += self.dic[f].count_participant(score)
        else:
            cnt += self.dic[food].count_participant(score)
    
        return cnt
        
class Food:
    
    def __init__(self):
        self.dic = defaultdict(int)
    
    def add_score(self, score):
        self.dic[int(score)] += 1
        
    def count_participant(self, std):
        std = int(std)
        cnt = 0
        
        # 문제: 매번 전체 비교를 하기 때문에 최악의 경우 100,000 * 50,000
        for k in self.dic.keys():
            if k >= std:
                cnt += self.dic[k]
            
        return cnt
        
        
def solution(info, query):
    participant = Participant()
    
    for p in info:
        lan, part, level, food, score = p.split(" ")
        participant.add_participant(lan, part, level, food, score)
    
    answer = []
    for q in query:
        qlist = q.split(" ")
        lan, part, level, food, score = qlist[0], qlist[2], qlist[4], qlist[6], qlist[7]
        answer.append(participant.count_participant(lan, part, level, food, score))
        
    return answer

# 이분탐색으로 결과 찾기
from collections import defaultdict

class Participant:
    lans = ["python", "cpp", "java"]
    
    def __init__(self):
        self.dic = dict()
        for l in self.lans:
            self.dic[l] = Lan()
            
    def add_participant(self, lan, part, level, food, score):
        if lan == "-":
            for l in self.lans:    
                self.dic[l].add_participant(part, level, food, score)
        else:
            self.dic[lan].add_participant(part, level, food, score)
        
    def count_participant(self, lan, part, level, food, score):
        cnt = 0
        if lan == "-":
            for l in self.lans:
                cnt += self.dic[l].count_participant(part, level, food, score)
        else:
             cnt += self.dic[lan].count_participant(part, level, food, score)
                
        return cnt
    
    def sort_score(self):
        for l in self.lans:
            self.dic[l].sort_score()
        
class Lan:
    part = ["backend", "frontend"]

    def __init__(self):
        self.dic = dict()
        for p in self.part:
            self.dic[p] = Part()
            
    def add_participant(self, part, level, food, score):
        if part == "-":
            for p in self.part:
                self.dic[p].add_participant(level, food, score)
        else:
            self.dic[part].add_participant(level, food, score)
            
    def count_participant(self, part, level, food, score):
        cnt = 0
        if part == "-":
            for p in self.part:
                cnt += self.dic[p].count_participant(level, food, score)
        else:
            cnt += self.dic[part].count_participant(level, food, score)
    
        return cnt
    
    def sort_score(self):
        for p in self.part:
            self.dic[p].sort_score()
                    
class Part:
    level = ["junior", "senior"]
    
    def __init__(self):
        self.dic = dict()
        for lv in self.level:
            self.dic[lv] = Level()
            
    def add_participant(self, level, food, score):
        if level == "-":
            for lv in self.level:
                self.dic[lv].add_participant(food, score)
        else:
            self.dic[level].add_participant(food, score)
            
    def count_participant(self, level, food, score):
        cnt = 0
        if level == "-":
            for lv in self.level:
                cnt += self.dic[lv].count_participant(food, score)
        else:
            cnt += self.dic[level].count_participant(food, score)
    
        return cnt
    
    def sort_score(self):
        for l in self.level:
            self.dic[l].sort_score()

class Level:
    food = ["pizza", "chicken"]
    
    def __init__(self):
        self.dic = dict()
        for f in self.food:
            self.dic[f] = Food()
            
    def add_participant(self, food, score):
        if food == "-":
            for f in self.food:
                self.dic[f].add_participant(score)
        else:
            self.dic[food].add_score(score)
            
    def count_participant(self, food, score):
        cnt = 0
        if food == "-":
            for f in self.food:
                cnt += self.dic[f].count_participant(score)
        else:
            cnt += self.dic[food].count_participant(score)
    
        return cnt
    
    def sort_score(self):
        for f in self.food:
            self.dic[f].sort_score()
        
class Food:
    
    def __init__(self):
        self.dic = defaultdict(int)
        self.keys = None
        self.prefix_sum_of_score = None
    
    def add_score(self, score):
        self.dic[int(score)] += 1
        
    def count_participant(self, std):
        std = int(std) 
        s, e, mid = 0, len(self.keys)-1, 0
        
        while s <= e:
            mid = (s+e) // 2
            
            # 기준 점수가 더 낮을 때
            if self.keys[mid] > std:
                s = mid + 1
            # 기준 점수랑 같을 때
            elif self.keys[mid] == std:
                e = mid
                break
            # 기준 점수가 더 높을 때
            else:
                e = mid - 1
            
        return 0 if e < 0 else self.prefix_sum_of_score[e]
    
    
    def sort_score(self):
        self.keys = sorted(list(self.dic.keys()), reverse = True)
        if self.keys:
            self.prefix_sum_of_score = [0] * len(self.keys)
            self.prefix_sum_of_score[0] = self.dic[self.keys[0]]

            for i in range(1, len(self.keys)):
                self.prefix_sum_of_score[i] = self.prefix_sum_of_score[i-1] + self.dic[self.keys[i]]
                
        
def solution(info, query):
    participant = Participant()
    
    for p in info:
        lan, part, level, food, score = p.split(" ")
        participant.add_participant(lan, part, level, food, score)
        
    participant.sort_score()
    
    answer = []
    for q in query:
        qlist = q.split(" ")
        lan, part, level, food, score = qlist[0], qlist[2], qlist[4], qlist[6], qlist[7]
        answer.append(participant.count_participant(lan, part, level, food, score))
        
    return answer

# 더 나은 풀이
def solution(info, query):
    data = dict()
    for a in ['cpp', 'java', 'python', '-']:
        for b in ['backend', 'frontend', '-']:
            for c in ['junior', 'senior', '-']:
                for d in ['chicken', 'pizza', '-']:
                    data.setdefault((a, b, c, d), list())
                    
    for i in info:
        i = i.split()
        for a in [i[0], '-']:
            for b in [i[1], '-']:
                for c in [i[2], '-']:
                    for d in [i[3], '-']:
                        data[(a, b, c, d)].append(int(i[4]))
                        
    for k in data:
        data[k].sort()
        
    answer = []
    for q in query:
        q = q.split()
        pool = data[(q[0], q[2], q[4], q[6])]
        find = int(q[7])
        
        l, r, mid = 0, len(pool), 0
        while l < r:
            mid = (r+l)//2
            if pool[mid] >= find:
                r = mid
            else:
                l = mid+1
                
        answer.append(len(pool) - l)
        
    return answer
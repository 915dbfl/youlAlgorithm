#21.02.05
#로또의 최고 순위와 최저 순위

def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]
    cnt = 0
    zero = lottos.count(0)
    
    for i in lottos:
        if i in win_nums:
            cnt += 1
            
    return rank[cnt + zero], rank[cnt]
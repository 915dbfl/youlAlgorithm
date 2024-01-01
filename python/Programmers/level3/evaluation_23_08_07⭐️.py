#인사고과

#틀린 풀이
def solution(scores):
    lst = []
    exp = []
    
    
    for i in range(len(scores)):
        lst.append([i, scores[i]])

    std = sorted(lst, key = lambda x: (x[1][0]))
    max_cscore = 0
    for i in range(1, len(scores)+1):
        if max_cscore > std[-i][1][1]:
            exp.append(std[-i][0])
        max_cscore = max(max_cscore, std[-i][1][1])
    
    rank  = sorted(std, key = lambda x: (sum(x[1])), reverse = True)
    max_sum = 100000
    ranking = person = 0
    for p, evals  in rank:
        if p not in exp:
            tmp_sum = sum(evals)
            if tmp_sum < max_sum:
                if p == 0:
                    return person + 1
                else:
                    max_sum = tmp_sum
                    ranking = person + 1
                    person += 1
            elif tmp_sum == max_sum:
                if p == 0:
                    return ranking
                else:
                    person += 1
    else:
        return -1
    

# 다른 풀이
def solution(scores):
    answer = 0
    target = scores[0]
    target_score = sum(scores[0])
    
    scores.sort(key = lambda x: (-x[0], x[1]))
    max_b = 0
    
    for score in scores:
        if target[0] < score[0] and target[1] < score[1]:
            return -1
        
        if max_b < score[1]:
            max_b = score[1]
            if sum(score) > target_score:
                answer += 1
                
    return answer + 1
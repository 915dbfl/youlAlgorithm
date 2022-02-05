#22.02.05
# 신고 결과 받기

def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))]
    reported_list = {x: 0 for x in id_list}
    
    for i in set(report):
        reported_list[i.split()[1]] += 1
    
    for j in set(report):
        x, y = j.split()
        if reported_list[y] >= k:
            answer[id_list.index(x)] += 1
            
    print(answer)
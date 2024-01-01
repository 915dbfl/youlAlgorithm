#22.05.27
#디스크 컨트롤러 : 힙

#내 풀이
def solution(jobs):
    l = len(jobs)
    jobs.sort()
    answer = jobs[0][1]
    time = jobs[0][0]+jobs[0][1] #작업이 끝나는 시간
    jobs.pop(0)
    
    while jobs:
        if jobs[0][0] < time:
            lst = list(filter(lambda x: x[0] < time, jobs))
            lst.sort(key = lambda x: x[1])
            answer += time+lst[0][1]-lst[0][0]
            time += lst[0][1]
            del(jobs[jobs.index(lst[0])])
            jobs.sort()
        else:
            answer += jobs[0][1]
            time = jobs[0][0]+jobs[0][1]
            jobs.pop(0)
    return answer//l
#22.06.14
#[1차] 셔틀버스

#내 풀이
def getTime(t):
    h = "0"+str(t//60) if t//60 < 10 else str(t//60)
    m = "0"+str(t%60) if t%60 < 10 else str(t%60)
    return h+":"+m

def solution(n, t, m, timetable):
    crews = []
    for x in timetable:
        lst = x.split(":")
        crews.append(int(lst[0])*60 + int(lst[1]))
    crews.sort()
    cur = 0
    for i in range(n):
        time = 540+i*t
        full = 0
        for _ in range(m):
            try:
                if crews[cur] <= time:
                    cur += 1
                else:
                    break
            except:
                return getTime(540+t*(n-1))
        else:
            full = 1
    if full:
        return getTime(crews[cur-1]-1)
    else:
        if crews[cur] > 540+t*(n-1):
            return getTime(540+t*(n-1))
        else:
            return getTime(crews[cur]-1)
# 누적합으로 계산
# 헷갈렸던 부분: 시청 종료 시간은 시청한 시간으로 포함하지 않는다!⭐️

def solution(play_time, adv_time, logs):
    def ss_to_time(ss):
        time = []
        h = ss // 3600
        time.append(h)
        m = (ss % 3600) // 60
        time.append(m)
        time.append((ss % 60))
        
        return ":".join(map(lambda x: str(x).zfill(2), time))
    
    def time_to_ss(h, m, s):
        return h * 3600 + m * 60 + s
    
    def cal_prefix(pf, logs):
        for log in logs:
            start, end = log.split("-")
            sh, sm, ss = map(int, start.split(":"))
            eh, em, es = map(int, end.split(":"))
            
            start_ss = time_to_ss(sh, sm, ss)
            end_ss = time_to_ss(eh, em, es)
            
            # 시청 시간 이상 / 미만
            pf[start_ss] += 1
            pf[end_ss] -= 1 
            
        for i in range(1, len(pf)):
            pf[i] += pf[i-1]
        
    ph, pm, ps = map(int, play_time.split(":"))
    total_ss = time_to_ss(ph, pm, ps)
    
    # 누적합 배열
    pf = [0] * (total_ss + 1)
    # log에 따른 누적합 계산
    cal_prefix(pf, logs)
    
    # 동영상 재생 시간 dp
    adh, adm, ads = map(int, adv_time.split(":"))
    adv_ss = time_to_ss(adh, adm, ads)

    max_play_time = sum(pf[:adv_ss])
    insert_time = 0
    cur_play_time = max_play_time
    
    # 최대 재생 시간 구하기
    for i in range(adv_ss, len(pf)):
        cur_play_time += pf[i] - pf[i - adv_ss]
        
        if cur_play_time > max_play_time:
            max_play_time = cur_play_time
            insert_time = i - adv_ss + 1

    # ss to time
    return ss_to_time(insert_time)
    
# refactoring
def s2i(s):
    h, m, s = map(int, s.split(":"))
    return h * 3600 + m * 60 + s

def i2s(t):
    ret = ''
    ret += str(t//3600).zfill(2)+':'
    t %= 3600
    ret += str(t//60).zfill(2)+':'
    t %= 60
    ret += str(t).zfill(2)
    return ret

def solution(play_time, adv_time, logs):
    pt, at = s2i(play_time), s2i(adv_time)
    d = [0]*360001
    for l in logs:
        st, en = map(s2i, l.split('-'))
        d[st] += 1
        d[en] -= 1
    for i in range(1, 360001):
        d[i] += d[i-1]
    mxval, mxtime = sum(d[:at]), 0
    curval = mxval
    # 360001 - at을 통해서 광고를 넣을 수 없는 부분은 제외함
    for i in range(1, 360001-at):
        curval = curval - d[i-1] + d[i+at-1]
        if curval > mxval:
            mxval = curval
            mxtime = i
    return i2s(mxtime)
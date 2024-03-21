# 누적합으로 계산
# 헷갈렸던 부분: 시청 종료 시간은 시청한 시간으로 포함하지 않는다!

# 초시간 가져오기
def get_time(time):
    h, m, s = map(int, time.split(":"))
    return h * 3600 + m * 60 + s

# 초시간 str 가져오기
def get_str_time(time):
    h = time // 3600
    m = (time % 3600) // 60
    s = (time % 3600) % 60
    
    h =  "0" + str(h) if h < 10 else str(h)
    m = "0" + str(m) if m < 10 else str(m)
    s = "0" + str(s) if s < 10 else str(s)

    return h + ":" + m + ":" + s

def solution(play_time, adv_time, logs):
    logs.sort()
    max_size = (3600 * 99) + (60 * 59) + 61
    prefix = [0] * (max_size)
    
    for log in logs:
        start, end = log.split("-")
        prefix[get_time(start)] += 1
        prefix[get_time(end)] -= 1
    
    # 구간 합 구하기
    for i in range(1, len(prefix)):
        prefix[i] += prefix[i-1]
        
    # 최대 누적 재생시간 구하기
    adv_time = get_time(adv_time)
    # 0부터 시작했을 때로 값 초기화
    sum_of_play = sum(prefix[:adv_time])
    sum_start = 0
    max_sum = sum_of_play
    max_sum_start = 0
    
    for i in range(adv_time, len(prefix)):
        sum_of_play += prefix[i]
        sum_of_play -= prefix[sum_start]
        sum_start += 1
        
        if sum_of_play > max_sum:
            max_sum = sum_of_play
            max_sum_start = sum_start
                
    play_time = get_time(play_time)
    if play_time - max_sum_start < adv_time:
        return get_str_time(play_time - adv_time)
    else:
        return get_str_time(max_sum_start)
    
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
# 1시간
def solution(m, musicinfos):
    answer = "(None)"
    ansT = 0
    ml = len(m)
    
    for music in musicinfos:
        start, end, title, code = music.split(",")
        
        # 시간 구하기
        sh, sm = map(int, start.split(":"))
        eh, em = map(int, end.split(":"))
        start = sh*60 + sm
        end = eh*60 + em
        
        # 코드 늘리기
        cn = len(code) - code.count("#")
        allCode = (end - start)//cn * code
        remainCn = (end - start) % cn
        p = 0
        while p < len(code) and remainCn > 0:
            allCode += code[p]
            if p < len(code)-1 and code[p+1] == "#":
                allCode += code[p+1]
                p += 1
            p += 1
            remainCn -= 1
    
        # 해당 음악에 기억한 멜로디가 포함되는 경우
        # ⛔️ 제일 처음 위치만 확인하면 안됨, 끝까지 다 확인해야 함
        idx = allCode.find(m)
        while idx >= 0:
            # #존재 파악
            idx += len(m)
            if ansT < (end - start):
                if idx >= len(allCode) or allCode[idx] != "#":
                    answer = title
                    ansT = end - start
            idx = allCode.find(m, idx+1)
            
    return answer

# 더 간단한 방법

# 복잡한 # 처리 대신 #이 달린 음계를 lower 값으로 치환!⭐️
def shap_to_lower(s):
    s = s.replace('C#','c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')
    return s

def solution(m, musicinfos):
    answer = [0, '(None)']
    m = shap_to_lower(m)
    
    for music in musicinfos:
        start, end, title, code = music.split(",")
        code = shap_to_lower(code)
        
        # 시간 구하기
        sh, sm = map(int, start.split(":"))
        eh, em = map(int, end.split(":"))
        time_length = (eh*60 + em) - (sh*60 + sm)
        
        # 전체 코드 구하기
        full_code = code * (time_length // len(code)) + code[:time_length % len(code)]
        
        # 기억나는 코드가 전체 코드에서 존재하는 지 확인
        if m in full_code and time_length > answer[0]:
            answer = [time_length, title]
            
    return answer[-1]
        
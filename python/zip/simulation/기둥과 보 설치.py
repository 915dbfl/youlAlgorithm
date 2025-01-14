"""
[풀이]
- 구현 문제
- 설치와 삭제할 때마다 구조물이 완전한지 확인해야 함
- 구조물 기록: set에 저장
"""

def check_frame(n, frames):
    for x, y, a in frames:
        check_flag = False
        if a == 0: # 기둥 확인
            if y == 0: # 바닥이거나
                check_flag = True
            # 보 한쪽 끝 위 or 기둥 위
            elif (x, y-1, 0) in frames or (x, y, 1) in frames or (x-1, y, 1) in frames:
                check_flag = True
        else: # 보 확인
            # 양쪽이 다른 보 끝에 연결 or 한쪽 아래에 기둥 존재
            if (x, y-1, 0) in frames or (x+1, y-1, 0) in frames or ((x-1, y, 1) in frames and (x+1, y, 1) in frames):
                check_flag = True

        if not check_flag:
            return False
    return True
        
def solution(n, build_frame):
    answer = set()
    for x, y, a, b in build_frame:
        if b == 1: # 설치
            answer.add((x, y, a))
        else: 
            answer.remove((x, y, a))
        
        # 완전한 구조물이 아닐 경우 rollback
        if not check_frame(n, answer):
            if b == 1: # 설치면 삭제
                answer.remove((x, y, a))
            else: # 삭제면 다시 설치
                answer.add((x, y, a))
                
    answer = list(answer)
    answer.sort()
    return answer
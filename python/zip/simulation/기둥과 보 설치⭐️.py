# 우선 설치와 삭제를 진행하고
# 전체적인 구조물을 확인 후 조건을 만족하지 못하면 rollback

def check_frame(answer):
    for x, y, a in answer:
        # 기둥
        if a == 0:
            # 바닥이 아니고
            # 좌표 아래에 기둥이 존재하지 않고
            # 보의 한쪽 끝에 있는게 아니라면
            if (y != 0 and
                [x, y-1, 0] not in answer and
                [x-1, y, 1] not in answer and
                [x, y, 1] not in answer):
                return False
        # 보
        elif a == 1:
            # 아래에 기둥이 존재하지 않고,
            # 양쪽에 보가 없다면
            if ([x, y-1, 0] not in answer and
                [x+1, y-1, 0] not in answer and
                ([x-1, y, 1] not in answer or
                 [x+1, y, 1] not in answer)):
                return False
    return True

def solution(n, build_frame):
    answer = []

    for x, y, a, b in build_frame:
        # 삭제
        if b == 0:
            answer.remove([x, y, a])
            # 삭제 후 구조물 체크
            if not check_frame(answer):
                answer.append([x, y, a])

        # 설치
        elif b == 1:
            answer.append([x, y, a])
            # 설치 후 구조물 체크
            if not check_frame(answer):
                answer.remove([x, y, a])

    answer.sort()
    return answer
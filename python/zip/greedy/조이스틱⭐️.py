# 오답
# dp
import sys
INF = sys.maxsize

def get_min_dis(cur, bf, l):
    min_dis = abs(cur - bf)
    if cur > bf:
        min_dis = min(min_dis, bf+l - cur)
    else:
        min_dis = min(min_dis, cur+l - bf)
        
    return min_dis

def get_min_dis_from_A(target):
    return min(ord(target) - ord("A"), ord("Z") - ord(target) + 1)

def solution(name):
    move = [0]*len(name)
    dp = [[[INF, []] for _ in range(len(name))] for _ in range(len(name))]
    answer = INF
    
    # 무조건 방문해야 하는 must_move 구하기
    must_move = set()
    for i in range(len(name)):
        if name[i] != "A":
            must_move.add(i)
    
    # move[i][j]: i번째 알파벳에서 j번째 알파벳으로 이동하기 위한 최소 이동값
    for i in range(len(name)):
        move[i] = get_min_dis_from_A(name[i])
            
    # dp[i][j] i번째 때 j에 방문할 경우 최소 이동
    # dp 초기값 세팅
    for i in range(len(name)):
        dp[0][i] = [i + move[i], [set([i])]]
    
    # time 번째 방문 확인
    for time in range(1, len(name)):
        # time 번째 방문일 떄 curd을 방문할 경우
        for cur in range(len(name)):
            # dp[time][cur]: time번째 때 cur를 방문할 경우 최소 이동 구하기
            min_move = INF
            for bf in range(len(name)):
                dis = get_min_dis(cur, bf, len(name))
                # dp[time-1][bf]의 모든 경로 확인
                for route in dp[time-1][bf][1]:
                        # route에 cur이 없다면
                        if cur not in route:
                            check_move = dp[time-1][bf][0] + dis + move[cur]
                            # dp값 업데이트
                            if dp[time][cur][0] > check_move:
                                dp[time][cur][0] = check_move
                                dp[time][cur][1] = [route | set([cur])]
                            elif dp[time][cur][0] == check_move:
                                dp[time][cur][1].append(route | set([cur]))
                                
                            if len((route | set([cur])) & must_move) == len(must_move):
                                answer = min(answer, check_move)
                                
    for case in dp[-1]:
        answer = min(answer, case[0])
    return answer

# 핵심
# 1. 모든 위치의 알파벳을 조작하는 cnt 전체 값은 바뀌지 않는다.
# 2. 어떻게 이동하냐가 핵심!
# 3. A가 연속되어 있다면 그 부분은 지나가지 않아도 된다.
# 4. A의 연속된 부분이 긴쪽을 안 지나가는 것이 유리!

def solution(name):
    # 조이스틱 조작 횟수
    answer = 0
    
    # 기본 최소 좌우이동 횟수는 길이 -1
    min_move = len(name)-1
    
    for i, char in enumerate(name):
        # 해당 알파벳 변경 최솟값 추가
        answer += min(ord(char) - ord("A"), ord("Z") - ord(char) +1)
        
        # 해당 알파벳 다음부터 연속된 A 문자열 찾기
        next = i+1
        while next < len(name) and name[next] == "A":
            next += 1
            
        # 기존, 연속된 A의 왼쪽 시작 방식, 연속된 A의 오른쪽 시작 방식 비교 및 갱신
        min_move = min([min_move, 2*i + len(name) - next, i + 2 * (len(name) - next)])
        
    answer += min_move
    return answer
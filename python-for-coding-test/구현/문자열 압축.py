# 2020 카카오 신입 공채

# 내 풀이
# 문자열 s를 size 단위로 자를 경우 결과를 구하는 함수
def checkSplit(s, size):
    result = 0
    length = len(s)
    cnt = 1
    start, end = size, size*2
    prev = s[:size]

    while start <= length-1 and end <= length :
        if prev == s[start: end]: # 같은 문자 반복
            cnt += 1
        else:
            if cnt > 1:
                result += len(str(cnt))
            result += len(prev)
            
            # 초기화
            cnt = 1
            prev = s[start: end]
            
        # start, end 업데이트
        start = end
        end = start + size
    
    # 마지막 처리
    if cnt > 1:
        result += len(str(cnt))
    result += len(prev)
      
    # 나머지 처리
    if start <= length-1:
        result += length - start

    return result

def solution(s):
    max_len = len(s) // 2
    result = len(s)
    
    # i 단위로 잘라 압축 진행
    for i in range(1, max_len + 1):
        tmp = checkSplit(s, i)
        if result > tmp:
            result = tmp
            
    return result

# 답안 예시

def solution(s):
    answer = len(s)

    # 1개 단위부터 압축 단위를 늘려가며 확인
    for step in range(1, len(s)//2 + 1):
        compressed = ""
        prev = s[0:step] # 앞에서부터 step만큼의 문자열 추출
        count = 1

        # 단위 크기만큼 증가시키며 이전 문자열과 비교
        for j in range(step, len(s), step):
            # 이전 상태와 동일하다면 압축 횟수 증가
            if prev == s[j: j+step]:
                count += 1
            # 다른 문자열이 나왔다면
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j:j+step] # 다시 상태 초기화
                count = 1
        # 남아 있는 문자열에 대해서 처리
        compressed += str(count) + prev if count >= 2 else prev
        # 만들어지는 압축 문자열이 가장 짧은 것이 정답
        answer = min(answer, len(compressed))

    return answer
def solution(s):
    answer = []
    for str in s:
        # 존재하는 모든 110 제거
        count, idx, stack = 0, 0, ""
        while idx < len(str):
            if str[idx] == "0" and stack[-2:] == "11":
                stack = stack[:-2]
                count += 1
            else:
                stack += str[idx]
            idx += 1
        
        # 110을 올바른 곳에 재배치
        idx = stack.find("111")
        # 111이 존재하지 않는다면
        # rfind로 가장 마지막에 나오는 0바로 뒤에 110 연속 배치
        # 1뒤에 배치할 경우 1110이 되어 111이 생기기 때문
        if idx == -1:
            idx = stack.rfind("0")
            answer.append(stack[:idx+1] + "110"*count + stack[idx+1:])
        # 111이 존재한다면
        # 해당 위치 바로 앞에 110 연속 배치
        else:
            answer.append(stack[:idx] + "110"*count + stack[idx:])
            
    return answer

# 참고: https://tiktaek.tistory.com/71
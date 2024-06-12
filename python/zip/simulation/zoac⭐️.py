import sys
input = sys.stdin.readline

def solution(s, start):
    global answer

    # 배열이 없으면 리턴
    if not s:
        return
    
    # 현재 배열의 제일 작은 알파벳을 찾는다.
    target = min(s)
    idx = s.index(target)

    # answer에 제일 작은 알파벳 위치에 제익 작은 알파벳을 추가
    answer[start + idx] = target
    print("".join(answer))

    solution(s[idx+1:], start + idx + 1)
    solution(s[:idx], start)

word = list(input().rstrip())
answer = [''] * len(word)
solution(word, 0)
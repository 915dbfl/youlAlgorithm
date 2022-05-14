#22.05.13
#JadenCase

#내 풀이
def solution(s):
    answer = []
    for i in s.split(" "):
        if i != "":
            tmp = i[0].upper() + i.lower()[1:]
            answer.append(tmp)
        else:
            answer.append("")
    return ' '.join(answer)

#다른 풀이: capitalize() 사용
#capitalize(): 문자열 첫글자만 대문자로, 나머지는 소문자로 변환한다.
#첫글자가 숫자일 경우, 그대로 둔다.
def solution(s):
    answer = []
    for i in s.split(" "):
        answer.append(i.capitalize())
    return ' '.join(answer)

#title()의 경우, 문자열 내 띄어쓰기를 기준으로 단어의 첫글자는 대문자로, 나머지는 소문자로 변환한다.
#단, 첫글자에 숫자가 있을 경우, 가장 처음으로 나오는 알파벳을 대문자로 바꾼다.
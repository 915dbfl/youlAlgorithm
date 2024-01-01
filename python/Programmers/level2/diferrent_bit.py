#22.04.18
#2개 이하로 다른 비트

#내 풀이
def solution(numbers):
    answer = []
    for i in numbers:
        if i % 2 == 0:
            answer.append(i+1)
        else:
            tmp = list(bin(i))
            for i in range(len(tmp)-1, 1, -1):
                if tmp[i] == '0':
                    tmp[i] = '1'
                    tmp[i+1] = '0'
                    answer.append(int(''.join(tmp), 2))
                    break
            else:
                answer.append(int("0b10" + '1'*(len(tmp)-3), 2))
    return answer
#bin(숫자) - 이진수 구하기
#int(숫자, 숫자의 형태) - 해당 형태의 수를 int형으로 변환한다.
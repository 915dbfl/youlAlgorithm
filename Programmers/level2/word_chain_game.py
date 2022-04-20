#22.04.20
#영어 끝말잇기

#내 풀이
def solution(n, words):
    used = [words[0]]
    for i in range(1, len(words)):
        if (words[i] in used) or (words[i-1][-1] != words[i][0]):
            p = i%n + 1
            t = i//n + 1
            return [p, t]
        else:
            used.append(words[i])
    else:
        return [0, 0]
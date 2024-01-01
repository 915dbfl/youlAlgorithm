#22.05.09
#최댓값과 최솟값

def solution(s):
    lst = list(map(int, s.split(" ")))
    return f'{min(lst)} {max(lst)}'
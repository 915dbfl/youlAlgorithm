"""
# 시간 복잡도
- size = info 사이즈
- O(size * n) = 40 * 120

# 풀이: dict를 활용한 dp
- 풀이를 본다면 dp를 진행할 때 1~n 모든 수를 확인하기 보다 유효한 값만 확인하면 됨
- 이차원 dp를 진행한다면 1~n을 모두 순환해야 하기 때문에 불필요한 순환이 진행됨
"""

def solution(info, n, m):
    adict = {0: 0}
    # i번째 물건을 a, b가 훔치는 경우 모두 고려
    for a, b in info:
        new_dict = {}
        for aa, ab in adict.items():
            # a가 훔칠 경우 - n을 넘어가는 경우는 생각하지 않음
            if aa + a < n:
                if aa + a not in new_dict or new_dict[aa+a] > ab:
                    new_dict[aa+a] = ab
            # b가 훔칠 경우 - m을 넘어가는 경우는 생각하지 않음
            if ab + b < m:
                if aa not in new_dict or new_dict[aa] > ab + b:
                    new_dict[aa] = ab + b
        if new_dict:
            adict = new_dict
        else:
            return -1
    return min(adict.keys())
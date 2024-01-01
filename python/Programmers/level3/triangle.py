#22.05.19
#정수 삼각형: 동적 계획법

#내 풀이
def solution(triangle):
    for i in range(1, len(triangle)):
        for j in range(0, len(triangle[i])):
            if j == 0:
                triangle[i][j] += triangle[i-1][j]
            elif j == len(triangle[i])-1:
                triangle[i][j] += triangle[i-1][j-1]
            else:
                triangle[i][j] +=  max(triangle[i-1][j-1], triangle[i-1][j])
    return max(triangle[-1])

#람다를 이용한 한 줄 풀이
solution = lambda t, l = [] : max(l) if not t else solution(t[1:], [max(x, y)+z for x, y, z in zip([0]+l, l+[0], t[0])])
# 한 층식 제거하며 최대 이동거리들을 계산에 l에 저장한다.
# t가 false일 경우, 모든 층을 거친 경우이므로 이동거리의 최대값인 max(l)을 출력한다.
# t가 존재할 경우, 이동거리를 계산해 solution을 재호출한다.
  # [0]+l, l+[0]를 통해서 처음과 끝 요소의 경우를 가운데 요소들과 동일하게 처리할 수 있게 된다.
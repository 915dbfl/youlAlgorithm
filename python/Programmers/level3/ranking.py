#22.06.02
#순위

#내 풀이: 그래프
def solution(n, results):
    graph = [[set(), set()] for _ in range(n+1)] #[w, d]
    for w, d in results:
        #이긴사람의 w업데이트
        graph[w][0] |= graph[d][0]|set([d])
        for i in graph[w][1]:
            graph[i][0] |= graph[w][0]
        #진사람의 d업데이트
        graph[d][1] |= graph[w][1]|set([w])
        for i in graph[d][0]:
            graph[i][1] |= graph[d][1]
    answer = 0
    lst = [i[0]|i[1] for i in graph]
    return len(list(filter(lambda x: len(x) == n-1, lst)))
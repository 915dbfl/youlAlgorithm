/*
# 주요 정보
- 모든 도시 사이에는 단 한 개의 경로만이 존재한다. => 트리
- 도로는 양방향
- 도로의 거리는 모두 1
- 소방서 최적의 위치
    - 소방서에서 다른 도시로 이동하는 거리 최대가 최소가 될 수 있도록

# 풀이 과정
- 각 노드에서 가장 먼 노드? => 트리의 지름의 양 끝 중 하나
- 트리의 지름 정가운데 노드가 정답이 된다.
 */

import kotlin.math.*

private class Solution12896(
    private val n: Int,
    private val graph: Array<ArrayList<Int>>,
) {
    private fun bfs(target: Int): Pair<Int, Int> {
        val dq = ArrayDeque<Int>()
        dq.add(target)
        val visited = IntArray(n+1) {Int.MAX_VALUE}
        visited[target] = 0
        
        var maxDist = 0
        var maxNode = 0

        while(dq.isNotEmpty()) {
            val cur = dq.removeLast()

            for (nxt in graph[cur]) {
                if (visited[nxt] == Int.MAX_VALUE) {
                    visited[nxt] = visited[cur] + 1
                    dq.add(nxt)

                    if (maxDist < visited[nxt]) {
                        maxDist = visited[nxt]
                        maxNode = nxt
                    }
                }
            }
        }
        return maxDist to maxNode
    }

    fun solve(): Int {
        // 임의의 값 1로부터 최대 거리의 노드 구하기
        var result = bfs(1)

        // 트리 지름 전체 구하기
        result = bfs(result.second)

        return (result.first + 1) / 2
    }
}

fun main() = with(System.`in`.bufferedReader()) {
    val n = readLine().toInt()
    val graph = Array(n+1) {ArrayList<Int>()}
    // 그래프 초기화
    repeat(n-1) {
        val (start, end) = readLine().split(" ").map {it.toInt()}
        graph[start].add(end)
        graph[end].add(start)
    }

    val solution = Solution12896(n, graph)
    println(solution.solve())
}
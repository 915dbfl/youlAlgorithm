import kotlin.math.*

private class Solution12978(
    private val n: Int,
    private val graph: Array<ArrayList<Int>>,
) {
    private val dp: Array<ArrayList<Int>> = Array(n+1) {arrayListOf(0, 1)}
    private val visited: BooleanArray = BooleanArray(n+1)

    private fun dfs(cur: Int) {
        for (nxt in graph[cur]) {
            if (!visited[nxt]) {
                visited[nxt] = true
                // 자식 노드 모두 순회
                dfs(nxt)

                // 현재 위치에 경찰서를 세우지 않는다면 다음 위치에 무조건 존재해야 함
                dp[cur][0] += dp[nxt][1]
                // 현재 위치에 경찰서를 세우면 다음 위치에 경찰서 존재 유무 상관 없음
                dp[cur][1] += dp[nxt].min()
            }
        }
    }

    fun solve(): Int {
        visited[1] = true
        dfs(1)

        return dp[1].min()
    }
}

fun main() = with(System.`in`.bufferedReader()) {
    val n = readLine().toInt()
    val graph = Array(n+1) {ArrayList<Int>()}

    repeat(n-1) {
        val (a, b) = readLine().split(" ").map {it.toInt()}
        graph[a].add(b)
        graph[b].add(a)
    }

    val solution = Solution12978(n, graph)
    println(solution.solve())
}
// 트리 dp
import java.io.*
import java.util.*
import kotlin.math.min

const val INF = Int.MAX_VALUE
lateinit var graph: Array<ArrayList<Int>>
lateinit var visited: BooleanArray
lateinit var dp: Array<ArrayList<Int>>
var answer = 0

fun main() = with(System.`in`.bufferedReader()) {
    val n = readLine().toInt()
    graph = Array(n+1){ArrayList()}
    visited = BooleanArray(n+1)

    repeat(n-1) {
        val (u, v) = readLine().split(" ").map {it.toInt()}
        graph[u].add(v)
        graph[v].add(u)
    }

    dp = Array(n+1){arrayListOf(0, 1)}
    dfs(1)
    print(dp[1].min())
}

fun dfs(cur: Int) {
    visited[cur] = true
    for (nxt in graph[cur]) {
        if (!visited[nxt]) {
            dfs(nxt)

            // 해당 위치에 경찰서를 세울 경우, 자식 노드에 경찰서를 세우는지 여부는 상관없음
            dp[cur][1] += min(dp[nxt][0], dp[nxt][1])
            // 해당 위치에 경찰서를 세우지 않을 경우, 자식 노드에 경찰서를 무조건 세워야 함
            dp[cur][0] += dp[nxt][1]
        }
    }
}
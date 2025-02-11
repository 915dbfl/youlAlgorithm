/*
# 문제 핵심
- 모든 컴퓨터 최소 길이로 연결
- 모두 연결 x -1 출력
- a-z 1~26 / A-Z 27~52

# 풀이 과정 - MST
 */
import java.util.PriorityQueue
import kotlin.system.exitProcess

data class Edge(val from: Int, val to: Int, val weight: Int) : Comparable<Edge> {
    override fun compareTo(other: Edge): Int {
        return this.weight - other.weight
    }
}

private class Solution1414(
    private val n: Int,
    costs: Array<Array<Int>>,
) {
    private var parent = IntArray(n + 1) { it }
    private var total = costs.sumOf { it.sum() }
    private val pq = PriorityQueue<Edge>()

    init {
        for (i in 0 until n) {
            for (j in 0 until n) {
                if (costs[i][j] > 0) {
                    pq.offer(Edge(i, j, costs[i][j]))
                }
            }
        }
    }

    fun find(x: Int): Int {
        return if (x == parent[x]) x
        else {
            parent[x] = find(parent[x])
            parent[x]
        }
    }

    fun union(x: Int, y: Int): Boolean {
        val nx = find(x)
        val ny = find(y)

        return if (nx != ny) {
            parent[nx] = ny
            true
        } else false
    }

    fun solve(): Int {
        while (pq.isNotEmpty()) {
            val target = pq.poll()
            if (union(target.to, target.from)) total -= target.weight
        }

        val firstParent = find(0)
        for (i in 1 until n) {
            if (firstParent != find(i)) {
                return -1
            }
        }

        return total
    }
}



fun main() = with(System.`in`.bufferedReader()) {
    val n = readLine().toInt()

    // 0 -> 0, a ~ z -> 1 ~ 26, A ~ Z -> 27 ~ 52
    val costs = Array(n) {
        val line = readLine()
        Array<Int>(n) {
            when {
                line[it].isDigit() -> 0
                line[it].isLowerCase() -> line[it] - 'a' + 1
                else -> line[it] - 'A' + 27
            }
        }
    }

    val solution1414 = Solution1414(n, costs)
    println(solution1414.solve())    
}
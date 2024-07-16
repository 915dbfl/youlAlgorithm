// 12분
import kotlin.collections.ArrayDeque

lateinit var graphWithCandies: Array<IntArray>

fun main() = with(System.`in`.bufferedReader()) {
    val (n, m) = readLine().split(" ").map {it.toInt()}
    graphWithCandies = Array(n) {
        readLine().split(" ").map {it.toInt()}.toIntArray()
    }

    println(bfs(n, m))
}

private fun bfs(n: Int, m: Int): Int {
    val result = Array(n) {IntArray(m)}
    val dx = arrayOf(1, 1, 0)
    val dy = arrayOf(0, 1, 1)
    result[0][0] = graphWithCandies[0][0]
    for (i in 0 until n) {
        for (j in 0 until m) {
            for (k in 0 until 3) {
                val nx = i + dx[k]
                val ny = j + dy[k]

                if (nx !in 0 until n || ny !in 0 until m) continue
                result[nx][ny] = maxOf(result[nx][ny], result[i][j] + graphWithCandies[nx][ny])
            }
        }
    }
    return result.last().last()
}
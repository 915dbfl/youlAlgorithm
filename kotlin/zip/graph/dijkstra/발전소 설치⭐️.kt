/*
풀이 과정
- 1~n까지 다익스트라
    - 각 정점 사이 거리 구하기
        - limit을 넘어갈 경우 무한대로 표시
        - 전선이 존재한다면 0으로 표시
    - 1을 기준으로 다익스트라 진행
 */

import java.util.PriorityQueue
import kotlin.math.*

private class Solution1277 {
    fun getDist(
        x1: Int,
        y1: Int,
        x2: Int,
        y2: Int,
    ): Double {
        return sqrt(abs(x1 - x2).toDouble().pow(2) + abs(y1 - y2).toDouble().pow(2))
    }

    fun solve(
        n: Int,
        dist: Array<DoubleArray>,
    ) {
        val pq = PriorityQueue<Pair<Double, Int>>(compareBy {it.first})
        val resultDist = DoubleArray(n+1) {Double.MAX_VALUE}
        pq.offer(0.0 to 1)
        resultDist[1] = 0.0

        while (pq.isNotEmpty()) {
            val(curD, curN) = pq.poll()

            if (resultDist[curN] < curD) continue

            for (nxt in 1 until n+1) {
                if (dist[curN][nxt] != Double.MAX_VALUE) {
                    val newDist = curD + dist[curN][nxt]
                    if (newDist < resultDist[nxt]) {
                        resultDist[nxt] = newDist
                        pq.offer(newDist to nxt)
                    }
                }
            }
        }

        println((resultDist[n] * 1000).toInt())
    }
}

fun main() = with(System.`in`.bufferedReader()) {
    val (n, w) = readLine().split(" ").map {it.toInt()}
    val m = readLine().toDouble()
    val solution1277 = Solution1277()

    val plants = Array(n) {
        readLine().split(" ").map {it.toInt()}.toIntArray()
    }

    val dist = Array(n+1) {
        DoubleArray(n+1) {Double.MAX_VALUE}
    }

    for (i in 1 until n+1) {
        for (j in 1 until n+ 1) {
            if (i == j) dist[i][j] = 0.0
            else {
                dist[i][j] = solution1277.getDist(plants[i-1][0], plants[i-1][1], plants[j-1][0], plants[j-1][1])
                if (dist[i][j] > m) {
                    dist[i][j] = Double.MAX_VALUE
                }
            }
        }
    }

    for (i in 0 until w) {
        val (n1, n2) = readLine().split(" ").map {it.toInt()}
        dist[n1][n2] = 0.0
        dist[n2][n1] = 0.0
    }

    solution1277.solve(n, dist)
}
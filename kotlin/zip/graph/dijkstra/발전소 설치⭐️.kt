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

private class Problem1277(
    n: Int,
    w: Int,
    limit: Double,
    plants: ArrayList<List<Int>>,
) {
    private val oneDist = DoubleArray(n+1) {Double.MAX_VALUE}

    fun solve(
        dist: Array<DoubleArray>,
    ): Int {
        val pq = PriorityQueue<Pair<Double, Int>>(compareBy {it.first})
        pq.offer(Pair(0.0, 1))
        oneDist[1] = 0.0

        while(pq.isNotEmpty()) {
            val (totalCost, node) = pq.poll()

            if (oneDist[node] < totalCost) continue

            for (i in 1 until dist.size) {
                val cost = dist[node][i]
                if (cost == Double.MAX_VALUE) continue

                val newCost = totalCost + cost
                if (newCost < oneDist[i]) {
                    oneDist[i] = newCost
                    pq.offer(Pair(newCost, i))
                }
            }
        }

        return (oneDist[dist.size-1] * 1000).toInt()
    }

    fun getDistance(
        x1: Int,
        y1: Int,
        x2: Int,
        y2: Int,
    ): Double {
        val bottom = abs(y2-y1)
        val top = abs(x2-x1)
        return sqrt(bottom.toDouble().pow(2) + top.toDouble().pow(2))
    }
}

fun main() = with(System.`in`.bufferedReader()) {
    val (n, w) = readLine().split(" ").map {it.toInt()}
    val limit = readLine().toDouble()
    val plants = arrayListOf<List<Int>>()
    val dist = Array(n+1) {
        DoubleArray(n+1) {Double.MAX_VALUE}
    }

    for (i in 0 until n) {
        plants.add(readLine().split(" ").map {it.toInt()})
    }

    val problem1277 = Problem1277(n, w, limit, plants)

    for (i in 1 until n+1) {
        for (j in 1 until n+1) {
            if (i == j) dist[i][j] = 0.0
            dist[i][j] = problem1277.getDistance(plants[i-1][0], plants[i-1][1], plants[j-1][0], plants[j-1][1])
            // limit보다 거리가 멀면, 무한 값을 넣음
            if (dist[i][j] >= limit) {
                dist[i][j] = Double.MAX_VALUE
            }
        }
    }
    
    for (i in 0 until w) {
        val (s, e) = readLine().split(" ").map {it.toInt()}
        dist[s][e] = 0.0
        dist[e][s] = 0.0
    }

    println(problem1277.solve(dist))
}
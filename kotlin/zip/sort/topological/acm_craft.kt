// 20분

import kotlin.collections.ArrayDeque

val bw = System.out.bufferedWriter()

lateinit var degree: IntArray
lateinit var child: Array<ArrayList<Int>>
lateinit var dur: IntArray

fun main() = with(System.`in`.bufferedReader()) {
    val t = readLine().toInt()
    repeat(t) {
        val (n, k) = readLine().split(" ").map {it.toInt()}
        child = Array(n+1){ArrayList<Int>()}
        dur = readLine().split(" ").map {it.toInt()}.toIntArray()
        degree = IntArray(n+1)

        repeat(k) {
            val (p, c) = readLine().split(" ").map {it.toInt()}
            child[p] += c
            degree[c]++    
        }

        val totalDis = calTotalDur(n)
        val target = readLine().toInt()

        bw.write("${totalDis[target]}\n")
    }
    bw.close()
}

fun calTotalDur(n: Int): IntArray {
    val dis = IntArray(n+1)
    val dq = ArrayDeque<Int>()

    // 시작점 구하기
    for (i in 1 until n+1) {
        if (degree[i] == 0) {
            dq.add(i)
            dis[i] = dur[i-1]
        }
    }

    while (dq.isNotEmpty()) {
        val cur = dq.removeFirst()

        for (ch in child[cur]) {
            dis[ch] = maxOf(dis[ch], dis[cur] + dur[ch-1])
            // 모든 업데이트가 끝난 후 큐에 넣는다.
            // 이렇게 하지 않으면 n이 1000이므로 시간 초과가 발생한다.
            if (--degree[ch] == 0) {
                dq.add(ch)
            }
        }
    }

    return dis
}
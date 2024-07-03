/*
1. IMPOSSIBLE: 사이클이 발생하는 경우
    - 위상정렬은 시작점이 존재해야 한다.
    - 사이클이 존재할 경우, 시작점이 없으므로 IMPOSSIBLE을 출력한다.

2. ?: queue에 두 개 이상의 원소가 들어있는 경우
    - 여러 요소간의 우위를 가릴 수 없는 경우
 */

import kotlin.collections.ArrayDeque

val br = System.`in`.bufferedReader()
val bw = System.out.bufferedWriter()

const val RESULT_IMPOSSIBLE = "IMPOSSIBLE"
const val RESULT_UNKOWN = "?"

var n = 0
lateinit var degree: IntArray
lateinit var edges: Array<BooleanArray>

fun solve() {
    n = br.readLine().toInt()
    val lastRank = br.readLine().split(" ").map {it.toInt()}.toIntArray()
    degree = IntArray(n+1)
    edges = Array(n+1){BooleanArray(n+1)}

    for((index, value) in lastRank.withIndex()) {
        degree[value] = index

        for (i in 0 until index) {
            edges[lastRank[i]][value] = true
        }

    }

    val m = br.readLine().toInt()
    repeat(m) {
        val (a, b) = br.readLine().split(" ").map {it.toInt()}
        swap(a, b)
    }

    bw.write("${topologicalSort()}\n")
}

fun topologicalSort(): String {
    val dq = ArrayDeque<Int>()
    var answer = ArrayList<Int>()

    for (i in 1 until n+1) {
        if (degree[i] == 0) {
            dq.add(i)
        }
    }

    // 정점 개수만큼 반복
    while(dq.isNotEmpty()){
        if (dq.size > 1) return RESULT_UNKOWN

        val cur = dq.removeFirst()
        answer.add(cur)

        for (k in 1 until n+1) {
            if (edges[cur][k]) {
                edges[cur][k] = false
                if(--degree[k] == 0) dq.add(k)
            }
        }
    }

    if (answer.size < n) return RESULT_IMPOSSIBLE

    return answer.joinToString(" ")
}

fun swap(n1: Int, n2: Int) {
    // n2가 n1보다 등수가 높을 경우
    if (!edges[n1][n2]) {
        edges[n1][n2] = true
        edges[n2][n1] = false
        degree[n2]++
        degree[n1]--
    // n1이 n2보다 등수가 높을 경우
    } else {
        edges[n2][n1] = true
        edges[n1][n2] = false
        degree[n1]++
        degree[n2]--
    }
}

fun main() {
    val testCnt = br.readLine().toInt()

    repeat(testCnt) {
        solve()
    }
    bw.close()
}
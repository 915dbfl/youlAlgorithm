// 원자의 에너지
// 30분
// 플로이드 워샬
fun main() = with(System.`in`.bufferedReader()) {
    val n = readLine().toInt()
    val graph = mutableListOf<IntArray>()
    repeat(n) {
        graph.add(readLine().split(" ").map {it.toInt()}.toIntArray())
    }

    floyd(n, graph)
}

private fun floyd(n: Int, graph: List<IntArray>) {
    val dis = mutableListOf<IntArray>()
    repeat(n) {
        dis.add(graph[it])
    }

    for (k in 0..<n) {
        for (i in 0..<n) {
            for (j in 0..<n) {
                if (dis[i][j] == 0 && (dis[i][k] == 1 && dis[k][j] == 1)) {
                    dis[i][j] = 1
                }
            }
        }
    }

    println(dis.joinToString("\n"){it.joinToString(" ")})
}

// 다른 풀이
// dfs

import java.io.BufferedReader
import java.io.InputStreamReader
import java.io.OutputStreamWriter
import java.io.BufferedWriter

lateinit var graph: MutableList<IntArray>
lateinit var disGraph: List<IntArray>
var curNode: Int = 0

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val bw = BufferedWriter(OutputStreamWriter(System.out))

    val n = br.readLine().toInt()
    graph = mutableListOf()
    disGraph = List(n) {IntArray(n)}
    repeat(n) {
        val row = br.readLine().split(" ").map{it.toInt()}.toIntArray()
        graph.add(row)
    }

    repeat(n) {
        curNode = it
        dfs(n, it)
    }

    bw.write(disGraph.joinToString("\n") {it.joinToString(" ")})
    bw.close()
}

private fun dfs(n: Int, startNode: Int) {
    for (i in 0..<n){
        if (graph[startNode][i] == 1 && disGraph[curNode][i] == 0) {
            disGraph[curNode][i] = 1
            dfs(n, i)
        }
    }
}
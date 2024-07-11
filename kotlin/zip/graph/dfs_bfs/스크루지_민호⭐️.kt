import java.util.ArrayDeque

lateinit var graph: Array<ArrayList<Int>>
var maxDis = -1
var maxDisIdx = -1

fun main() = with(System.`in`.bufferedReader()) {
    val n = readLine().toInt()
    var answer = n+1
    graph = Array(n+1) {ArrayList<Int>()}

    repeat(n-1) {
        val (c1, c2) = readLine().split(" ").map {it.toInt()}
        graph[c1].add(c2)
        graph[c2].add(c1)
    }
    
    maxDis = -1
    bfs(n, 1)

    maxDis = -1
    bfs(n, maxDisIdx)

    println(Math.ceil(maxDis.toDouble()/2).toInt())
}

fun bfs(n: Int, start: Int) {
    val dis = IntArray(n+1)
    val dq = ArrayDeque<Int>()
    dq.add(start)

    while (dq.isNotEmpty()) {
        val cur = dq.removeFirst()
        maxDis = dis[cur]
        maxDisIdx = cur

        for (nxt in graph[cur]) {
            if (nxt != start && dis[nxt] == 0) {
                dis[nxt] = dis[cur]+1
                dq.add(nxt)
            }
        }
    }
    // println(dis.joinToString())
    // println("$maxDis $maxDisIdx")
}
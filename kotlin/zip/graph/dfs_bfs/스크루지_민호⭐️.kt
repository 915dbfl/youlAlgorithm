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
    
    // 1에서 걸리는 최대 거리 idx를 구함
    // 해당 idx에는 소방서가 무조건 존재하지 않음
    maxDis = -1
    bfs(n, 1)

    // 해당 idx를 기준으로 가장 먼 거리 중간에 소방서가 위치해야 함
    maxDis = -1
    bfs(n, maxDisIdx)

    println(Math.ceil(maxDis.toDouble()/2).toInt())
    //println((maxDis + 1)/2)
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
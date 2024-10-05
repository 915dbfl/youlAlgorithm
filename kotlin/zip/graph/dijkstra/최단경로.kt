import java.util.PriorityQueue

lateinit var graph: List<MutableList<Node>>

data class Node(val index: Int, val distance: Int)

fun main() = with(System.`in`.bufferedReader()) {
    val (v, e) = readLine().split(" ").map {it.toInt()}
    val start = readLine().toInt()
    graph = List(v+1) { mutableListOf<Node>() }

    repeat(e) {
        val (u, v, w) = readLine().split(" ").map {it.toInt()}
        graph[u].add(Node(v, w))
    } 

    val result = djikstra(v, start).drop(1)
    for (i in 0..<result.size) {
        if (result[i] != Int.MAX_VALUE) {
            println(result[i])
        } else {
            println("INF")
        }
    }
    
}

fun djikstra(v: Int, start: Int): IntArray {
    val pq = PriorityQueue<Node>( compareBy {it.distance} )
    val result = IntArray(v+1) {Int.MAX_VALUE}
    result[start] = 0
    pq.add(Node(start, 0))

    while(pq.isNotEmpty()) {
        val cur = pq.remove()
        
        if (cur.distance > result[cur.index]) continue
        result[cur.index] = cur.distance

        for (nxtNode in graph[cur.index]) {
            if (nxtNode.distance + cur.distance < result[nxtNode.index]) {
                result[nxtNode.index] = nxtNode.distance + cur.distance
                pq.add(Node(nxtNode.index, nxtNode.distance + cur.distance))
            }
        }
    }

    return result
}
import java.io.*
import java.util.*
import kotlin.collections.ArrayList

private lateinit var graph: MutableList<MutableList<Node>>
private val dist = IntArray(10001) {INF}
private const val INF = Int.MAX_VALUE

data class Node(val index: Int, val dist: Int): Comparable<Node> {
    override fun compareTo(other: Node): Int = dist - other.dist
}

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val (n, d) = br.readLine().split(" ").map {it.toInt()}

    graph = ArrayList()
    for (i in 0 until d) {
        graph.add(ArrayList())
        graph[i].add(Node(i+1, 1))
    }

    for(i in 0..n-1) {
        val (start, end, dist) = br.readLine().split(" ").map {it.toInt()}

        // 역주행 불가
        if(end > d) continue

        // 원래 가는 길보다 지름길이 더 긴 경우
        if(dist >= (end - start)) continue

        graph[start].add(Node(end, dist))
    }

    dijkstra(d)
    print(dist[d])
}

private fun dijkstra(d: Int) {
    val q = PriorityQueue<Node>()
    q.offer(Node(0, 0))
    dist[0] = 0

    while(q.isNotEmpty()) {
        val poll = q.poll()

        if((poll.dist > dist[poll.index]) or (poll.index >= d)) continue

        val size = graph[poll.index].size
        for(i in 0..size-1) {
            val nextNode = graph[poll.index][i]

            if(dist[nextNode.index] > dist[poll.index] + nextNode.dist) {
                dist[nextNode.index] = dist[poll.index] + nextNode.dist
                q.offer(Node(nextNode.index, dist[nextNode.index]))
            }
        }
    }
}
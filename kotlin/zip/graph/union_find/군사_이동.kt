// 1시간
// dfs: O(p+w)
lateinit var graph: Array<ArrayList<Pair<Int, Int>>>
lateinit var visited: IntArray
const val MAX_WIDTH = 1001
var maxNWidth = 0

fun main() = with(System.`in`.bufferedReader()) {
    val (p, w) = readLine().split(" ").map {it.toInt()}
    val (bc, cc) = readLine().split(" ").map {it.toInt()}
    graph = Array(p) {ArrayList<Pair<Int, Int>>()}
    visited = IntArray(p)

    repeat(w) {
        val (ws, we, ww) = readLine().split(" ").map {it.toInt()}
        graph[ws].add(we to ww)
        graph[we].add(ws to ww)
    }

    dfs(bc, cc, MAX_WIDTH)
    println(maxNWidth)
}

fun dfs(cur: Int, goal: Int, curMin: Int) {
    // 정답보다 최솟값이 작은 경우
    if (curMin <= maxNWidth) return

    // 구해진 최솟값보다 최소 값이 작은 경우
    if (visited[cur] > curMin) return

    if (cur == goal) {
        maxNWidth = maxOf(maxNWidth, curMin)
    } else {
        for (nxt in graph[cur]) {
            val tmpMin = minOf(curMin, nxt.second)
            if (visited[nxt.first] < tmpMin) {                
                visited[nxt.first] = tmpMin
                dfs(nxt.first, goal, tmpMin)
            }
        }
    }
}

// 유니온 - 파인드 알고리즘
import java.util.PriorityQueue

data class Edge(val from: Int, val to: Int, val weight: Int)

lateinit var parent: IntArray

fun main() = with(System.`in`.bufferedReader()) {
    val (p, w) = readLine().split(" ").map {it.toInt()}
    val (c1, c2) = readLine().split(" ").map {it.toInt()}

    val pq = PriorityQueue<Edge> {a, b -> b.weight - a.weight}
    repeat(w) {
        val (w1, w2, w3) = readLine().split(" ").map {it.toInt()}
        pq.offer(Edge(w1, w2, w3))
    }

    parent = IntArray(p+1) {it}
    while(pq.isNotEmpty()) {
        val (from, to, wieght) = pq.poll()
        union(from, to)
        if (find(c1) == find(c2)) {
            println(wieght)
            return
        }
    }
}

fun find(x: Int): Int {
    if (parent[x] == x) return x
    else {
        parent[x] = find(parent[x])
        return parent[x]
    }
}

fun union(x: Int, y: Int) {
    val (px, py) = find(x) to find(y)
    if (px < py) {
        parent[py] = px
    } else {
        parent[px] = py
    }
}
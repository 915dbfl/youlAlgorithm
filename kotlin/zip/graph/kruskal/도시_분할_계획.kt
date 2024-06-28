// 30분
// 최소 신장 트리

val br = System.`in`.bufferedReader()
val bw = System.out.bufferedWriter()

lateinit var roadList: ArrayList<IntArray>
lateinit var parent: IntArray
var answer = 0

fun union(target1: Int, target2: Int) {
    val parent1 = parent[target1]
    val parent2 = parent[target2]

    if (parent1 < parent2) {
        parent[parent2] = parent[parent1]
    } else {
        parent[parent1] = parent[parent2]
    }
}

fun findParent(target: Int): Int {
    if (parent[target] == target) return target
    else {
        parent[target] = findParent(parent[target])
        return parent[target]
    }
}

fun divideCity(): Int {
    var lastRoad = 0
    for (road in roadList) {
        if (findParent(road[0]) != findParent(road[1])) {
            lastRoad = road[2]
            answer += road[2]
            union(road[0], road[1])
        }
    }  

    return answer - lastRoad
}

fun main() = with(System.out.bufferedWriter()) {
    val (n, m) = br.readLine().split(" ").map { it.toInt() }
    roadList = ArrayList<IntArray>()
    parent = IntArray(n+1) {it}

    repeat(m) {
        val road = br.readLine().split(" ").map {it.toInt()}.toIntArray()
        roadList.add(road)
    }

    roadList.sortWith(compareBy{it[2]})

    val result = divideCity()
    write("$result")
    close()
}

// PriorityQueue 풀이

import java.util.PriorityQueue

val br = System.`in`.bufferedReader()

fun main() = with(System.out.bufferedWriter()) {
    val (n, m) = br.readLine().split(" ").map {it.toInt()}
    val graph = Array(n+1) {mutableListOf<Pair<Int, Int>>()}
    val visited = BooleanArray(n+1)
    val queue = PriorityQueue<Pair<Int, Int>> {o1, o2 -> o1.second - o2.second}

    repeat(m) {
        val (s, e, c) = br.readLine().split(" ").map {it.toInt()}
        graph[s].add(e to c)
        graph[e].add(s to c)
    }

    var cnt = 0
    var ans = 0
    var max = 0

    queue.add(1 to 0)
    while(queue.isNotEmpty()) {
        val (cur, cost) = queue.poll()

        if(visited[cur]) continue

        visited[cur] = true
        cnt++
        ans += cost

        if(max < cost) 
            max = cost

        if (cnt == n)
            break

        // 컬렉션으로 복사
        graph[cur].filterNot {visited[it.first]}.toCollection(queue)
    }

    write("${ans - max}")
    close()
}
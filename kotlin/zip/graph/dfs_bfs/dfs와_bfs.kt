import java.io.*
import java.util.*

private lateinit var visited: BooleanArray
private lateinit var graph: Array<MutableList<Int>>
private val bw = BufferedWriter(OutputStreamWriter(System.out))

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    
    val (n, m, v) = br.readLine().split(" ").map {it.toInt()}
    graph = Array(n+1) {mutableListOf<Int>()}

    repeat(m) {
        val (s, e) = br.readLine().split(" ").map {it.toInt()}
        graph[s].add(e)
        graph[e].add(s)
    }

    for (i in graph) {
        i.sortDescending()
    }

    visited = BooleanArray(n+1)
    dfs(v)

    bw.write("\n")

    for (i in graph) {
        i.sort()
    }
    
    visited = BooleanArray(n+1)
    bfs(v)

    bw.flush()
    bw.close()

}

fun dfs(v: Int) {
    val q = ArrayDeque<Int>()
    q.add(v)

    while(q.isNotEmpty()) {
        val cur = q.removeLast()
        if (visited[cur]) {
            continue
        }
    
        bw.write("$cur ")
        visited[cur] = true

        for (i in graph[cur]) {
            if (!visited[i]) {
                q.add(i)
            }
        }
    }

    // visited[v] = true
    // bw.write("$v ")

    // for (i in graph[v]) {
    //     if (!visited[i]) {
    //         dfs(i)
    //     }
    // }
}

fun bfs(v: Int) {
    val q = ArrayDeque<Int>()
    q.add(v)
    visited[v] = true

    while(q.isNotEmpty()) {
        val cur = q.removeFirst()
        bw.write("$cur ")

        for (i in graph[cur]) {
            if (!visited[i]) {
                visited[i] = true
                q.add(i)
            }
        }
    }
}
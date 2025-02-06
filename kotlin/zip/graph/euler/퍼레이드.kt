private class Solution16168(private val n: Int) {
    private val parents = IntArray(n+1) {it}
    private val graph = Array(n+1) {ArrayList<Int>()}

    fun setConnection(a: Int, b: Int) {
        graph[a].add(b)
        graph[b].add(a)

        if (findParent(a) != findParent(b)) {
            union(a, b)
        }
    }

    private fun findParent(target: Int): Int {
        if (parents[target] != target) {
            parents[target] = findParent(parents[target])
        }
        return parents[target]
    }

    private fun union(n1: Int, n2: Int) {
        val p1 = findParent(n1)
        val p2 = findParent(n2)

        if (p1 < p2) {
            parents[p2] = p1
        } else {
            parents[p1] = p2
        }
    }

    fun solve(): String{
        // 그래프가 분리되었는지 확인 -> "NO"
        val parent = parents[1]
        for (i in 2 until n+1) {
            if (findParent(parents[i]) != parent) {
                return "NO"
            }
        }

        // 오일러 경로 / 회로 조건 확인
        val edge = ArrayList<Int>()
        for (i in 1 until n+1) {
            if (graph[i].size % 2 == 1) {
                edge.add(i)
            }
        }
        // 무방향 그래프에서는
        // 차수가 모두 짝수이거나(오일러 회로)
        // 차수가 홀수인 정점이 두 개여야 한다.(오일러 경로)
        return if (edge.size == 0 || edge.size == 2) "YES" else "NO"
    }
}


fun main() = with(System.`in`.bufferedReader()) {
    val (v, e) = readLine().split(" ").map {it.toInt()}
    val solution16168 = Solution16168(v)

    repeat(e) {
        val (v1, v2) = readLine().split(" ").map {it.toInt()}
        solution16168.setConnection(v1, v2)
    }

    println(solution16168.solve())
}
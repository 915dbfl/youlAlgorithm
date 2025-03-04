import kotlin.math.* 

private class Solution4315 {
    private lateinit var beadsCnt: IntArray 
    private lateinit var childCnt: IntArray 
    private lateinit var nodes: ArrayList<Node> 
    private lateinit var visited: BooleanArray 

    private fun dfs(cur: Int) { 
        beadsCnt[cur-1] += nodes[cur-1].beadsCnt 

        // 리프 노드일 경우 
        if (nodes[cur-1].childCnt == 0) { 
            return 
        } 

        for (nxt in nodes[cur-1].childs) { 
            if (!visited[nxt-1]) { 
                visited[nxt-1] = true 
                dfs(nxt) 
                beadsCnt[cur-1] += beadsCnt[nxt-1] 
                childCnt[cur-1] += childCnt[nxt-1] 
            } 
        } 
    } 

    private fun getRoot(nodes: ArrayList<Node>): Int { 
        val degree = IntArray(nodes.size+1) 

        for (node in nodes) { 
            for (child in node.childs) { 
                degree[child] += 1 
            } 
        } 

        var root = -1 
        for (i in 1..nodes.size) { 
            if (degree[i] == 0) { 
                root = i 
                break 
            } 
        } 

        return root 
    } 

    private fun minMove(): Int { 
        var answer = 0 

        for (i in 0 until nodes.size) { 
            answer += abs(childCnt[i] - beadsCnt[i]) 
        } 

        return answer 
    } 

    fun solve(nodes: ArrayList<Node>): Int { 
        this.nodes = nodes 
        beadsCnt = IntArray(nodes.size) 
        childCnt = IntArray(nodes.size) {1} 
        visited = BooleanArray(nodes.size) 

        val root = getRoot(nodes) 
        dfs(root) 
        return minMove() 
    } 
}

data class Node( 
    val v: Int, 
    val beadsCnt: Int, 
    val childCnt: Int, 
    val childs: List<Int>,
) 

fun main() = with(System.`in`.bufferedReader()) { 
    val solution = Solution4315() 

    while (true) { 
        val n = readLine().toInt() 
        val nodes = ArrayList<Node>() 

        if (n == 0) { 
            return 
        } else { 
            repeat(n) { 
                val infos = readLine().split(" ").map {it.toInt()}.toIntArray() 

                val node = Node( 
                    infos[0], 
                    infos[1], 
                    infos[2], 
                    infos.drop(3) 
                ) 
                nodes.add(node) 
            } 
            println(solution.solve(nodes)) 
        } 
    } 

}


// 리팩토링
import kotlin.math.abs

data class Node(
    val v: Int,
    val beadsCnt: Int,
    val childs: List<Int>
) {
    var visited = false
    var beadsSum = beadsCnt
    var childSum = 1
    var moveCount = 0

    fun dfs(nodes: List<Node>) {
        visited = true
        for (childIndex in childs.map { it - 1 }) {
            val child = nodes[childIndex]
            if (!child.visited) {
                child.dfs(nodes)
                beadsSum += child.beadsSum
                childSum += child.childSum
            }
        }
        moveCount = abs(childSum - beadsSum)
    }
}

fun List<Node>.getRoot(): Int {
    val degree = IntArray(size)
    forEach { node ->
        node.childs.forEach { child ->
            degree[child-1]++
        }
    }
    return degree.indexOfFirst { it == 0 }
}

fun solve(nodes: List<Node>): Int {
    val rootIndex = nodes.getRoot()
    nodes[rootIndex].dfs(nodes)
    return nodes.sumOf { it.moveCount }
}

fun main() = with(System.`in`.bufferedReader()) {
    generateSequence { readLine()?.toInt() }
        .takeWhile { it != 0 }
        .forEach { n ->
            val nodes = List(n) {
                val infos = readLine().split(" ").map { it.toInt() }
                Node(infos[0], infos[1], infos.drop(3))
            }
            println(solve(nodes))
        }
}
// 위상정렬: 오답
/*
1 -> 2
 \
  -> 3 -> 4

4 3
1 2
1 3
3 4
1
2 4

여기서 2, 4의 전후관계는 알 수 없음. 하지만 위상 정렬로 할 경우, -1이 출력됨
 */

import kotlin.collections.ArrayDeque

lateinit var degree: IntArray
lateinit var graph: Array<ArrayList<Int>>

fun main() = with(System.`in`.bufferedReader()) {
    val (n, k) = readLine().split(" ").map {it.toInt()}
    degree = IntArray(n+1)
    graph = Array(n+1){ArrayList<Int>()}

    repeat(k) {
        val (case1, case2) = readLine().split(" ").map {it.toInt()}
        degree[case2]++
        graph[case1].add(case2)
    }

    val order = topologicalSort(n)
    val s = readLine().toInt()
    repeat(s) {
        val (case1, case2) = readLine().split(" ").map {it.toInt()}
        if (order[case1] < order[case2]) {
            println(-1)
        } else if(order[case1] > order[case2]) {
            println(1)
        } else {
            println(0)
        }
    }
}

fun topologicalSort(n: Int): IntArray {
    val dq = ArrayDeque<Pair<Int, Int>>()
    val order = IntArray(n+1)

    for (i in 1..n) {
        if (degree[i] == 0) {
            dq.add(i to 0)
        }
    }

    while(dq.isNotEmpty()) {
        val cur = dq.removeFirst()
        order[cur.first] = cur.second

        for (nxt in graph[cur.first]) {
            degree[nxt]--
            if (degree[nxt] == 0) {
                dq.add(nxt to cur.second+1)
            }
        } 
    }

    return order
}

// 일일히 bfs로 확인하기
// 메모리 초과
// 시간 복잡도: O(S * (V+E) * 2)
import kotlin.collections.ArrayDeque

lateinit var graph: Array<ArrayList<Int>>

fun main() = with(System.`in`.bufferedReader()) {
    val (n, k) = readLine().split(" ").map {it.toInt()}
    graph = Array(n+1){ArrayList<Int>()}

    repeat(k) {
        val (case1, case2) = readLine().split(" ").map {it.toInt()}
        graph[case1].add(case2)
    }

    val s = readLine().toInt()
    repeat(s) {
        val (case1, case2) = readLine().split(" ").map {it.toInt()}
        println(checkOrder(case1, case2))
    }
}

fun checkOrder(num1: Int, num2: Int): Int {
    return if (isChild(num1, num2)) {
        -1
    } else if (isChild(num2, num1)) {
        1
    } else {
        0
    }
}

fun isChild(num1: Int, num2: Int): Boolean {
    val dq = ArrayDeque<Int>()
    dq.add(num1)

    while(dq.isNotEmpty()) {
        val cur = dq.removeFirst()

        for (nxt in graph[cur]) {
            if (nxt == num2) {
                return true
            }
            dq.add(nxt)
        }
    }

    return false
}

// 플로이드 워샬 알고리즘
// 시간복잡도: O(V^3)
import kotlin.collections.ArrayDeque

lateinit var childGraph: Array<BooleanArray>

fun main() = with(System.`in`.bufferedReader()) {
    val (n, k) = readLine().split(" ").map {it.toInt()}
    childGraph = Array(n+1){BooleanArray(n+1)}

    repeat(k) {
        val (case1, case2) = readLine().split(" ").map {it.toInt()}
        childGraph[case1][case2] = true
    }

    floyd(n)
    val s = readLine().toInt()
    repeat(s) {
        val (case1, case2) = readLine().split(" ").map {it.toInt()}
        if (childGraph[case1][case2]) {
            println(-1)
        } else if (childGraph[case2][case1]) {
            println(1)
        } else {
            println(0)
        }
    }
}

fun floyd(n: Int) {
    for (k in 1..n) {
        for (i in 1..n) {
            for (j in 1..n) {
                if (!childGraph[i][j] && (childGraph[i][k] && childGraph[k][j])) {
                    childGraph[i][j] = true
                }
            }
        }
    }
}
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

// 오답 - 레벨로는 사건 전후 관계를 알 수 없음

import java.util.*

private class Solution1613(
    val n: Int,
    val degree: IntArray,
    val child: Array<ArrayList<Int>>,
) {
    private val parent = IntArray(n+1) {it}
    private val level = IntArray(n+1) {Int.MAX_VALUE}

    init {
        for (i in 1 until n+1) {
            // 상위 사건이 없는 경우
            if (degree[i] == 0) {
                if (child[i].size > 0) {
                    // dfs로 level 기록
                    dfs(i)
                }
            }
        }
    }

    private fun find(a: Int): Int {
        if (parent[a] == a) {
            return parent[a]
        }
        return find(parent[a])
    }

    private fun union(a: Int, b: Int) {
        val parentA = find(a)
        val parentB = find(b)

        if (parentA < parentB) {
            parent[parentB] = parentA
        } else {
            parent[parentA] = parentB
        }
    }

    private fun dfs(start: Int) {
        val deque = ArrayDeque<Int>()
        deque.add(start)
        level[start] = 0

        while(!deque.isEmpty()) {
            val cur = deque.removeFirst()

            for (ch in child[cur]) {
                if (find(cur) != find(ch)) {
                    union(cur, ch)
                }
                if (level[ch] == Int.MAX_VALUE) {
                    level[ch] = Math.min(level[ch], level[cur] + 1)
                    deque.add(ch)
                }
            }
        }
    }

    fun solve(c1: Int, c2: Int): Int {
        val parentC1 = find(c1)
        val parentC2 = find(c2)

        if (parentC1 != parentC2) {
            return 0
        } else {
            return if (level[c1] < level[c2]) {
                -1
            } else if (level[c1] == level[c2]) {
                0
            } else {
                1
            }
        }
    }
}

fun main() = with(System.`in`.bufferedReader()) {
    var tokenizer = StringTokenizer(readLine())
    val n = tokenizer.nextToken().toInt()
    val k = tokenizer.nextToken().toInt()
    val degree = IntArray(n+1)
    val child: Array<ArrayList<Int>> = Array(n+1) {arrayListOf<Int>()}

    repeat(k) {
        tokenizer = StringTokenizer(readLine())
        val before = tokenizer.nextToken().toInt()
        val after = tokenizer.nextToken().toInt()
        degree[after] += 1
        child[before].add(after)
    }

    val solution1613 = Solution1613(n, degree, child)
    val s = readLine().toInt()
    repeat(s) {
        tokenizer = StringTokenizer(readLine())
        val c1 = tokenizer.nextToken().toInt()
        val c2 = tokenizer.nextToken().toInt()

        println(solution1613.solve(c1, c2))
    }
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
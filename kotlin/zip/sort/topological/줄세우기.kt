// 30분, 위상 정렬

import kotlin.collections.ArrayDeque

val br = System.`in`.bufferedReader()
fun main() = with(System.out.bufferedWriter()) {
    val (n, m) = br.readLine().split(" ").map {it.toInt()}
    // 번호, 해당 번호 앞에 나와야 할 번호 개수
    val studentMap = hashMapOf<Int, Int>()
    // 번호, 해당 번호 뒤에 나올 번호 리스트
    val nextMap = hashMapOf<Int, ArrayList<Int>>()

    repeat(m) {
        val (a, b) = br.readLine().split(" ").map {it.toInt()}
        if (studentMap.containsKey(b)) {
            studentMap[b] = studentMap[b]!! + 1
        } else {
            studentMap[b] = 1
        }
        if (nextMap.containsKey(a)) {
            nextMap[a]!!.add(b)
        } else {
            nextMap[a] = arrayListOf(b)
        }
    }

    val dq = ArrayDeque<Int>()
    for (i in 1 until n+1){
        if (!studentMap.containsKey(i)) {
            dq.add(i)
        }
    }

    val answer = ArrayList<Int>()
    while (dq.isNotEmpty()) {
        val cur = dq.removeLast()
        answer.add(cur)

        if (nextMap.containsKey(cur)) {
            for (nxt in nextMap[cur]!!) {
                if (studentMap.containsKey(nxt)) {
                    studentMap[nxt] = studentMap[nxt]!! - 1
                    if (studentMap[nxt]!! <= 0) {
                        dq.add(nxt)
                    }
                }
            }
        }
    }

    write("${answer.joinToString(" ")}")
    close()

}

// 다른 풀이
import java.util.LinkedList
import java.util.Queue

val br = System.`in`.bufferedReader()

fun main() = with(System.out.bufferedWriter()) {
    val (n, m) = br.readLine().split(" ").map {it.toInt()}

    val graph = Array(n+1) {mutableListOf<Int>()}
    val edgeCnt = IntArray(n+1)

    for (i in 0 until m) {
        val (a, b) = br.readLine().split(" ").map{it.toInt()}
        graph[a].add(b)
        edgeCnt[b]++ // 진입차수 기록
    }

    var queue = LinkedList<Int>() as Queue<Int>
    var answer = StringBuilder()

    // 진입차수 0인 값을 큐에 넣음
    for (i in 1 until n) {
        if (edgeCnt[i] == 0) {
            queue.offer(i)
        }
    }

    while(!queue.isEmpty()) {
        var student = queue.poll()

        answer.append(student).append(" ")

        for(i in 0 until graph[student].size - 1) {
            var back = graph[student][i]
            edgeCnt[back]--

            if (edgeCnt[back] == 0) {
                queue.offer(back)
            }
        }
    }

    write("$answer")
    close()
}
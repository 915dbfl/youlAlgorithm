// 우선순위 큐

import java.util.PriorityQueue
data class Meeting(
    val startTime: Int,
    val endTime: Int
)

val br = System.`in`.bufferedReader()
fun main() = with(System.out.bufferedWriter()) {
    val n = br.readLine().toInt()
    var timeTable = Array(n) {
        val (s, e) = br.readLine().split(" ").map {it.toInt()}
        Meeting(s, e)
    }

    val sortedTimeTable = timeTable.sortedWith(compareBy({it.startTime}, {it.endTime}))
    val timeDeque = PriorityQueue<Int>()

    // var answer = 0
    // for (case in sortedTimeTable) {
    //     // 현재 시작 시간보다 빨리 끝나는 경우 모두 제거
    //     while(timeDeque.isNotEmpty() && timeDeque.peek() <= case.startTime) {
    //         timeDeque.poll() // 우선순위가 가장 높은 값을 뺀다.
    //     }
    //     // 현재 끝나는 시간을 넣음
    //     timeDeque.offer(case.endTime)
    //     answer = answer.coerceAtLeast(timeDeque.size)
    // }

    // write("$answer")
    // close()

    for (case in sortedTimeTable) {
        // 현재 시작 시간보다 빨리 끝나는 경우 제거
        if (timeDeque.isNotEmpty() && timeDeque.peek() <= case.startTime) {
            timeDeque.poll()
        }
        // 현재 끝나는 시간을 넣음
        timeDeque.offer(case.endTime)
    }

    write("${timeDeque.size}")
    close()
    
}
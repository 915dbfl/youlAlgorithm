import kotlin.collections.ArrayDeque

val br = System.`in`.bufferedReader()
fun main() = with(System.out.bufferedWriter()) {
    val apple = br.readLine().toCharArray()
    val lover = br.readLine().toCharArray()
    val n = apple.size

    apple.sort()
    lover.sortDescending()

    val appleDeque = ArrayDeque<Char>()
    // appleDeque.addAll(apple.slice(IntRange(0, n-n/2)))
    for (i in 0 until (n - (n/2))) {
        appleDeque.add(apple[i])
    }
    val loverDeque = ArrayDeque<Char>()
    for (i in 0 until n/2) {
        loverDeque.add(lover[i])
    }

    val answer = CharArray(n)
    var start = 0
    var end = n-1
    repeat(n) {
        // 구사과 차례
        if (it % 2 == 0) {
            // apple의 가장 작은 수보다 lover의 가장 큰 수가 작을 경우
            if (loverDeque.isNotEmpty() && appleDeque.first() >= loverDeque.first()) {
                answer[end] = appleDeque.removeLast()
                end--
            } else {
                answer[start] = appleDeque.removeFirst()
                start++
            }

        // 큐브러버 차례
        } else {
            // apple의 가장 작은 수가 lover의 가장 큰 수보다 클 경우
            if (!appleDeque.isEmpty() && appleDeque.first() >= loverDeque.first()) {
                answer[end] = loverDeque.removeLast()
                end--
            } else {
                answer[start] = loverDeque.removeFirst()
                start++
            }
        }
    }

    write("${answer.joinToString("")}")
    close()
}
var result = 0
val base = setOf(1, 2, 3)
val sb = StringBuilder()

fun main() = with(System.`in`.bufferedReader()) {
    val n = readLine().toInt()
    hanoi(n, 1, 3)
    println(result)
    print(sb)
}

fun hanoi(target: Int, start: Int, end: Int) {
    if (target == 1) {
        result += 1
        sb.append("$start $end\n")
        return
    } else {
        val nextEnd = (base - setOf(start, end)).first()
        hanoi(target-1, start, nextEnd)
        result += 1
        sb.append("$start $end\n")
        hanoi(target-1, nextEnd, end)
    }
}
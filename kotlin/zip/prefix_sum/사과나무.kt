// 1시간
// 부루트포스 알고리즘 + 누적합

val br = System.`in`.bufferedReader()
val bw = System.out.bufferedWriter()
var n = 0
var answer = -90000000
lateinit var boardDp: Array<IntArray>

// 시간복잡도 - O(N^3)
fun getMaxDp() {
    for (i in 1 until n+1) {
        for (j in 1 until n+1) {
            val minL = i.coerceAtMost(j)
            val base = boardDp[i][j]
            for (k in 0 until minL) {
                val minusDp = boardDp[i-k-1][j] + boardDp[i][j-k-1] - boardDp[i-k-1][j-k-1]
                answer = maxOf(answer, base - minusDp)
            }
        }
    }

    bw.write("$answer")
    bw.close()
}

fun dpInit() {
    for (i in 1 until n+1) {
        for (j in 1 until n+1) {
            boardDp[i][j] += boardDp[i-1][j] + boardDp[i][j-1] - boardDp[i-1][j-1]
        }
    }
    // println(boardDp.joinToString("\n") {it.joinToString()})
}

fun input() {
    n = br.readLine().toInt()
    boardDp = Array(n+1) {IntArray(n+1)}
    repeat(n) {
        boardDp[it+1] = intArrayOf(0) + br.readLine().split(" ").map {it.toInt()}.toIntArray()
    }
}

fun main() {
    input()
    dpInit()
    getMaxDp()
}
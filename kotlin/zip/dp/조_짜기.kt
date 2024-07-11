// 30분
fun main() = with(System.`in`.bufferedReader()) {
    val n = readLine().toInt()
    val score = readLine().split(" ").map {it.toInt()}.toIntArray()

    val dp = IntArray(n+1)
    for (i in 2 until n+1) {
        var maxNum = score[i-1]
        var minNum = score[i-1]
        for (j in i downTo 1) {
            maxNum = maxOf(maxNum, score[j-1])
            minNum = minOf(minNum, score[j-1])

            dp[i] = maxOf(dp[i], dp[j-1] + (maxNum - minNum))
        }
    }

    println(dp.last())
}
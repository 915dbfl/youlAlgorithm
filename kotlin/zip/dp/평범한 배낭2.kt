/*
풀이과정 - 모든 자연수는 2의 배수의 합으로 나타낼 수 있다.
- 물건 N을 2의 배수들의 합으로 나타내기
    - 1, 2, 4, 8 ...로 나누어 아이템에 추가하기
- dp로 최대 만족도 구하기
 */

import kotlin.math.*

fun main() = with(System.`in`.bufferedReader()) {
    val (n, m) = readLine().split(" ").map {it.toInt()}
    val items = ArrayList<Pair<Int, Int>>()

    for (i in 0 until n) {
        val (v, c, k) = readLine().split(" ").map {it.toInt()}
        var i = 1
        var newK = k
        while (newK > 0) {
            val m = min(i, newK)
            items.add(v*m to c*m)
            newK -= i
            i *= 2
        }
    }

    val dp = IntArray(m+1)
    for ((v, c) in items) {
        for (i in m downTo v) {
            dp[i] = max(dp[i], dp[i-v] + c)
        }
    }

    print(dp[m])
}
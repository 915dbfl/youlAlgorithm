// 30분

import kotlin.math.*

fun main() = with(System.`in`.bufferedReader()) {
    val (n, k) = readLine().split(" ").map {it.toInt()}
    val items = Array(n) {
        readLine().split(" ").map {it.toInt()}.toIntArray()
    }

    val dp = Array(n) {IntArray(k+1)}
    val (fw, fv) = items[0]
    for (i in fw until k+1) {
        dp[0][i] = fv
    }

    for (i in 1 until n) {
        val (w, v) = items[i]
        for (j in 1 until k+1) {
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            if (j >= w) {
                dp[i][j] = max(dp[i][j], dp[i-1][j-w] + v)
            }
        }
    }

    println(dp[n-1][k])
}

// 일차원 배열 사용하기

fun main() = with(System.`in`.bufferedReader()) {
    val (n, k) = readLine().split(" ").map {it.toInt()}
    val items = Array(n) {
        readLine().split(" ").map {it.toInt()}.toIntArray()
    }

    val dp = IntArray(k+1)
    for ((w, v) in items) {
        for (i in k downTo w) {
            dp[i] = maxOf(dp[i], dp[i-w] + v)
        }
    }

    println(dp[k])
}
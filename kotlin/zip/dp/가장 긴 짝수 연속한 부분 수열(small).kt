import kotlin.math.max

// 가장 긴 짝수 연속한 부분 수열(small)
// 38분
// 투 포인터, dp

fun main() = with(System.`in`.bufferedReader()) {
    val (n, k) = readLine().split(" ").map {it.toInt()}
    val nums = readLine().split(" ").map {it.toInt()}.toIntArray()

    // 짝수, 홀수
    var dp: MutableList<Pair<Int, Int>> = mutableListOf(0 to 0)
    dp.add(if (nums[0] % 2 == 0) 1 to 0 else 0 to 1)
    for (i in 1..<n) {
        if (nums[i] % 2 == 0) {
            dp.add(dp[dp.size-1].first + 1 to dp[dp.size-1].second)
        } else {
            dp.add(dp[dp.size-1].first to dp[dp.size-1].second + 1)
        }
    }

    var left = 0
    var right = 0
    var answer = 0
    while(right <= n && left <= n) {
        if (dp[right].second - dp[left].second == k) {
            answer = max(answer, dp[right].first - dp[left].first)
            right++
        } else if (dp[right].second - dp[left].second < k) {
            right++
        } else {
            left++
        }
    }

    while(left <= n) {
        if (dp[n].second - dp[left].second <= k) {
            answer = max(answer, dp[n].first - dp[left].first)
        }
        left++
    }

    println(answer)
}
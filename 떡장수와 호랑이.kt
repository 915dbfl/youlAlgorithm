"""
1. 떡 종류는 어제와 달라야 한다. 
2. n번째 날까지 호랑이에게 떡을 줄 수 있다면 특정 경우만 출력하면 된다.
3. 모든 경우를 파악하면 시간 초과가 발생한다.


"""


fun main() = with(System.`in`.bufferedReader()) {
    val n = readLine().toInt()

    val dp = Array<IntArray>(n) {IntArray(10)}
    var total = 0
    var bTotal = 0

    repeat(n) { day ->
        val riceCakes = readLine().split(" ").map {it.toInt()}.toIntArray()
        for (rc in 1 until riceCakes.size) {
            if (day == 0) {
                dp[day][rc] = 1
                bTotal += 1
            } else {
                dp[day][rc] = total - dp[day-1][rc]
                bTotal += dp[day][rc]
            }
        }

        println("$total $bTotal")
        total = bTotal
        bTotal = 0
    }

    println(dp.joinToString {it.joinToString(" ")})
}
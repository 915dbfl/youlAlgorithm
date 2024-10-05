fun main() = with(System.`in`.bufferedReader()) {
    val (k, n) = readLine().split(" ").map {it.toInt()}
    val lines = IntArray(k) {
        readLine().toInt()
    }
    var left = 1L
    var right = lines.max().toLong()
    var maxLen = 0L

    while (left <= right) {
        // Int = 2^31
        // 해당 부분에서 Int범위가 벗어나기 때문에 Long으로 선언해줘야 한다.
        val mid = (left + right) / 2

        var tmpCnt = 0L
        for (line in lines) {
            tmpCnt += line / mid
        }
        if (n > tmpCnt) {
            right = mid - 1
        } else {
            left = mid + 1
            maxLen = mid
        }
    }

    print(maxLen)
}
// 중앙값
// 타입 제대로 지정하기⭐️

fun main() = with(System.`in`.bufferedReader()) {
    val n = readLine().toInt()
    var total_count = 0L
    val villages = Array(n) {
        val (index, head_count) = readLine().split(" ").map {it.toInt()}
        total_count += head_count
        Village(index, head_count)
    }

    villages.sortBy {it.index}

    var cur_count = 0L
    for (village in villages) {
        cur_count += village.head_count
        if (cur_count >= ((total_count + 1) / 2)) {
            println(village.index)
            return
        }
    }
}

data class Village(
    val index: Int,
    val head_count: Int,
)
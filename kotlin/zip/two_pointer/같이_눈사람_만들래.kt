// 22분
import kotlin.math.abs

lateinit var snowball: IntArray

fun main() = with(System.`in`.bufferedReader()) {
    val n = readLine().toInt()
    snowball = readLine().split(" ").map {it.toInt()}.toIntArray()

    val combis = combination(n)
    combis.sortWith(compareBy {snowball[it.first] + snowball[it.second]})
    println(getMinDiff(combis))
}

private fun combination(n: Int): ArrayList<Pair<Int, Int>> {
    val result = ArrayList<Pair<Int, Int>>()
    for(i in 0 until n) {
        for (j in i+1 until n) {
            result.add(i to j)
        }
    }

    return result
}

private fun getMinDiff(combis: ArrayList<Pair<Int, Int>>): Int {
    var minDiff = Int.MAX_VALUE

    for (i in 0 until combis.size-1) {
        val (sn1, sn2) = combis[i]
        val (sn3, sn4) = combis[i+1]

        if (sn1 != sn3 && sn1 != sn4 && sn2 != sn3 && sn2 != sn4) {
            minDiff = minOf(minDiff, abs((snowball[sn1] + snowball[sn2]) - (snowball[sn3] + snowball[sn4])))
        }
    }

    return minDiff
}

// 투포인터 풀이
import kotlin.math.abs

fun main() = with(System.`in`.bufferedReader()) {
    val n = readLine().toInt()
    val snowballs = readLine().split(" ").map{it.toInt()}.toIntArray()
    snowballs.sort()

    var min = Int.MAX_VALUE

    for (eljaLeft in 0 until n-3) {
        for (eljaRight in eljaLeft + 3 until n) {
            val eljaHeight = snowballs[eljaLeft] + snowballs[eljaRight]
            var left = eljaLeft + 1
            var right = eljaRight - 1
            while(left < right) {
                val height = snowballs[left] + snowballs[right]
                if (height < eljaHeight) {
                    left += 1
                } else if (height > eljaHeight) {
                    right -= 1
                } else {
                    println(0)
                    return
                }

                min = minOf(abs(eljaHeight - height), min)
            }
        }
    }

    println(min)
}
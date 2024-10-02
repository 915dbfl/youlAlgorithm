import kotlin.math.max
import kotlin.math.min

lateinit var nums: IntArray
lateinit var opCntList: IntArray

var maxValue = Int.MIN_VALUE
var minValue = Int.MAX_VALUE

fun main() = with(System.`in`.bufferedReader()) {
    val n = readLine().toInt()
    nums = readLine().split(" ").map { it.toInt() }.toIntArray()
    opCntList = readLine().split(" ").map { it.toInt() }.toIntArray()

    calculate(nums[0], 1)
    println(maxValue)
    println(minValue)
}

private fun calculate(total: Int, index: Int) {
    if (index >= nums.size) {
        maxValue = max(maxValue, total)
        minValue = min(minValue, total)
        return
    }

    for (i in opCntList.indices) {
        if (opCntList[i] <= 0) continue

        opCntList[i]--
        when(i) {
            0 -> calculate(total + nums[index], index + 1)
            1 -> calculate(total - nums[index], index + 1)
            2 -> calculate(total * nums[index], index + 1)
            else -> {
                if (total < 0) {
                    calculate(-(-total / nums[index]), index + 1)
                } else {
                    calculate(total / nums[index], index + 1)
                }
            }
        }
        opCntList[i]++
    }
}
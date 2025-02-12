private class Solution12015(
    private val n: Int,
    private val nums: IntArray
) {
    private val result = ArrayList<Int>()

    private fun searchIdx(target: Int): Int {
        var s = 0
        var e = result.size

        while (s <= e) {
            val mid = (s + e) / 2

            if (result[mid] == target) {
                return mid
            } else if(result[mid] < target) {
                s = mid + 1
            } else {
                e = mid - 1
            }
        }

        return s
    }

    fun solve(): Int {
        for (i in 0 until n) {
            val target = nums[i]

            if (result.size == 0 || target > result[result.size - 1]) {
                result.add(target)
            } else {
                val idx = searchIdx(target)
                result[idx] = target
            }
        }

        return result.size
    }
}

fun main() = with(System.`in`.bufferedReader()) {
    val n = readLine().toInt()
    val nums = readLine().split(" ").map {it.toInt()}.toIntArray()
    val solution12015 = Solution12015(n, nums)
    println(solution12015.solve())
}
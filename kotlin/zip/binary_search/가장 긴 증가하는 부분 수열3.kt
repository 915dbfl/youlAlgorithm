private class Solution12738 {
    fun solve(
        nums: IntArray,
    ): Int {
        val answer = ArrayList<Int>()
        answer.add(nums[0])

        for (i in 1 until nums.size) {
            if (answer.last() < answer[i]) {
                answer.add(nums[i])
            } else {
                val index = searchIndex(nums[i], answer)
                answer[index] = nums[i]
            }
        }

        return answer.size
    }

    fun searchIndex(
        target: Int,
        arr: ArrayList<Int>,
    ): Int {
        var start = 0
        var end = arr.size - 1
        var mid: Int

        while (start <= end) {
            mid = (start + end) / 2

            if (arr[mid] == target) {
                return mid
            } else if (arr[mid] > target) {
                end = mid - 1
            } else {
                start = mid + 1
            }
        }

        return start
    }
}

fun main() = with(System.`in`.bufferedReader()) {
    val n = readLine().toInt()
    val nums = readLine().split(" ").map {it.toInt()}.toIntArray()

    println(Solution12738().solve(nums))
}
/*
풀이 과정 - 1시간
1. ArrayDeque 활용
    - queue의 마지막 수가 크거나 같을 때 까지 pop
    - i번째 수 queue 넣기
2. index가 넘어갔을 때 정답 length 주의하기
 */

import kotlin.collections.ArrayDeque

private class Solution2812 {
    fun solution(
        n: Int,
        k: Int,
        nums: IntArray
    ): String {
        val stack = ArrayDeque<Int>()

        var index = 1
        var rmCnt = 0
        stack.add(nums[0])

        if (n == k) {
            return "0"
        }

        while(index < n) {
            while(rmCnt < k && stack.isNotEmpty()) {
                if (stack.last() < nums[index]) {
                    stack.removeLast()
                    rmCnt += 1
                } else break
            }
            if (rmCnt == k) break
            stack.add(nums[index])
            index += 1
        }

        var answer: String = buildString {
            append(stack.joinToString(""))
            append(nums.sliceArray(index..nums.lastIndex).joinToString(""))
        }
        
        if (answer.length > (n - k)) {
            answer = answer.substring(0 until n - k)
        }
        return answer
    }
}

fun main() = with(System.`in`.bufferedReader()) {
    var (n, k) = readLine().split(" ").map {it.toInt()}
    val nums = readLine().map {it.toString().toInt()}.toIntArray()

    println(Solution2812().solution(n, k, nums))
}
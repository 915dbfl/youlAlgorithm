/*
풀이 과정
1. 이진수의 각 자리수를 몇 번 더해야 할까?
    -> xor을 통해 몇 번 1이 되는지 구하면 됨
    -> xor 1이 되기 위해서는 서로 다른 값이 나와야 함
    -> 각 자리수의 0과 1의 개수 곱만큼 1이 된다.
    -> 이진수의 각 자리 수 * 1의 개수 * 0의 개수
 */

import kotlin.math.*

private class Solution2830(
    private val names: Array<String>,
) {
    private val zero = IntArray(20)
    private val one = IntArray(20)

    fun solve(): Int {
        for (name in names) {
            val bi = Integer.toBinaryString(name.toInt())
            for (i in bi.length - 1 downTo 0) {
                if (bi[i] == '0') {
                    zero[bi.length - i - 1]++
                } else {
                    one[bi.length - i - 1]++
                }
            }
            for (i in bi.length until 20) {
                zero[i]++
            }
        }
        
        var answer = 0
        for (i in 0 until 20) {
            val base = 2.0.pow(i).toInt()
            answer += base * zero[i] * one[i]
        }
        return answer
    }
}

fun main() = with(System.`in`.bufferedReader()) {
    val n = readLine().toInt()
    val names = Array(n) { readLine() }

    val solution = Solution2830(names)
    println(solution.solve())
}
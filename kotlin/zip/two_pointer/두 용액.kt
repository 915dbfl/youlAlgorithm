// 40분

/*
주요 정보
1. 산성 용액 특성값 1 - 10억
2. 알칼리성 용액 특성값 (-1) - (-10억)
3. 얻고자 하는 결과: 두 용액을 혼합해 0에 가장 가까운 용액 구하기

풀이 과정
1. 용액 특성 값 정렬 - nlogn
2. 투포인터로 해당 값 만들 수 있는지 확인 - n
 */

import kotlin.math.*

private class Solution2470 (
    private val rates: IntArray,
) {
    fun findTwoSolution(): Pair<Int, Int> {
        var start = 0
        var end = rates.size - 1
        var answer = 2e9.toInt()
        var solutions = -1 to -1

        while (start < end) {
            val result = rates[start] + rates[end]
            val diff = abs(result)
            if (diff < answer) {
                answer = diff
                solutions = rates[start] to rates[end]
            }

            if (result <= 0) {
                start += 1
            } else {
                end -= 1
            }
        }

        return solutions
    }
    
    fun solve(): Pair<Int, Int>{
        // 정렬
        rates.sort()
        
        // 정답 찾기
        return findTwoSolution()
    }
}

fun main() = with(System.`in`.bufferedReader()) {
    val n = readLine().toInt()
    val rates = readLine().split(" ").map {it.toInt()}.toIntArray()

    val solution = Solution2470(rates)
    val answer = solution.solve()
    println("${answer.first} ${answer.second}")
}

// 이분 탐색 풀이

import kotlin.math.*

private class Solution2470 (
    private val rates: IntArray,
) {
    fun binarySearch(sv: Int, target: Int): Int {
        var start = sv
        var end = rates.size - 1

        while (start <= end) {
            val mid = (start + end) / 2

            if (rates[mid] == target) {
                return mid
            } else if  (rates[mid] > target) {
                end = mid - 1
            } else {
                start = mid + 1
            }
        }
        return if (start <= rates.size-1) start else rates.size - 1
    }
    
    fun solve(): Pair<Int, Int>{
        rates.sort()
        
        var answer = -1 to -1
        var diff = 2 * (10.0.pow(9)).toInt()
        for (i in 0 until rates.size - 1) {
            val pairIdx = binarySearch(i+1, rates[i] * -1)

            if (diff > abs(rates[pairIdx] + rates[i])) {
                diff = abs(rates[pairIdx] + rates[i])
                answer = rates[i] to rates[pairIdx]
            }

            if ((pairIdx - 1 != i) && (diff > abs(rates[pairIdx - 1] + rates[i]))) {
                diff = abs(rates[pairIdx - 1] + rates[i])
                answer = rates[i] to rates[pairIdx - 1]
            }
        }

        return answer
    }
}

fun main() = with(System.`in`.bufferedReader()) {
    val n = readLine().toInt()
    val rates = readLine().split(" ").map {it.toInt()}.toIntArray()

    val solution = Solution2470(rates)
    val answer = solution.solve()
    println("${answer.first} ${answer.second}")
}
/*
해설
- 모든 경우의 수를 다 파악 -> 30C5
- 각 경우가 조건을 만족하는지 확인 30C5 * 10(조건의 최대 개수)
- 가능한 경우의 수 count => answer
*/

const val LENGTH = 5

class Solution {
    
    private var answer: Int = 0
    fun solution(n: Int, q: Array<IntArray>, ans: IntArray): Int {
        return countCombinations(n, 0, IntArray(LENGTH), q, ans)
    }
    
    private fun countCombinations(
        n: Int,
        k: Int,
        currentCombination: IntArray,
        q: Array<IntArray>,
        ans: IntArray,
    ): Int {
        if (k == LENGTH) {
            return if (isValidCombination(currentCombination, q, ans)) 1 else 0
        }
    
        var count = 0
        val startNum = if (k == 0) 1 else currentCombination[k-1] + 1
        
        for(i in startNum..n - (LENGTH - (k + 1))) {
            currentCombination[k] = i
            count += countCombinations(n, k + 1, currentCombination, q, ans)
        }
        
        return count
    }
    
    private fun isValidCombination(
        combi: IntArray, 
        q: Array<IntArray>, 
        ans: IntArray
    ): Boolean {
        val combiSet = combi.toSet()
        q.forEachIndexed { index, query ->
            var countMatches = 0
            for (ch in query) {
                if (combiSet.contains(ch)) {
                    countMatches += 1
                }
            }
            if(countMatches != ans[index]) {
                return false
            }
        }
        return true
    }
}
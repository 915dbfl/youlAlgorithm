import kotlin.math.*

class Solution {
    fun solution(a: Int, b: Int, g: IntArray, s: IntArray, w: IntArray, t: IntArray): Long {
        var start = 0L
        var end = 2 * (10.0.pow(9).toLong()) * 2 * (10.0.pow(5).toLong())
        var answer = end
        
        while(start <= end) {
            val mid = (start + end)/2
            var gold = 0L
            var silver = 0L
            var total = 0L
            
            for (i in 0 until g.size) {
                // 시간 내 운반할 수 있는 최대 횟수 구하기
                var maxCnt = mid / (t[i] * 2)
                if ((mid - maxCnt * (t[i] * 2)) > t[i]) {
                    maxCnt += 1
                }
                
                gold += min(w[i] * maxCnt, g[i].toLong())
                silver += min(w[i] * maxCnt, s[i].toLong())
                total += min(w[i] * maxCnt, (g[i] + s[i]).toLong())
            }
            
            if (gold >= a && silver >= b && total >= a+b) {
                end = mid - 1
                answer = min(answer, end)
            } else {
                start = mid + 1
            }
        }
        
        return answer
    }
}
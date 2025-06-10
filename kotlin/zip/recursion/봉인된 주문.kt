/*
해설
- n 글자 주문: 26^n개
- n에 해당하는 글자 구하기
    - n % 26을 통해 1의 자리 글자 파악
    - n / 26 진행 후 위의 과정 반복
- n에 해당하는 글자 이전에 존재하는 ban 개수 파악
*/

const val ALPHA_SIZE = 26

class Solution {

    fun solution(n: Long, bans: Array<String>): String {
        // 시간 복잡도: 300,000 * log(300,000) * 11(문자 최대 길이)
        val dq = ArrayDeque<String>(bans.sortedWith(compareBy<String>({it.length}, {it})))
        var targetN = n
        var alphaNum = getAlphaFromNum(targetN)
    
        while (!dq.isEmpty()) {
            val minBan = dq.first()
            if (minBan.length < alphaNum.length) {
                dq.removeFirst()
                targetN += 1
                alphaNum = getAlphaFromNum(targetN)
            } else if (minBan.length == alphaNum.length) {
                if (minBan <= alphaNum) {
                    dq.removeFirst()
                    targetN += 1
                    alphaNum = getAlphaFromNum(targetN)
                } else break
            } else break
        }
        
        return alphaNum
    }
    
    private fun getAlphaFromNum(num: Long): String {
        if(num <= ALPHA_SIZE) {
            val realNum = if (num == 0L) 26 else num
            return ('a' + (realNum.toInt() - 1)).toString()
        }
        
        val lastAlphaNum = num % ALPHA_SIZE
        val remainAlphaNum = if(lastAlphaNum == 0L) num / ALPHA_SIZE - 1 else num / ALPHA_SIZE
        return getAlphaFromNum(remainAlphaNum) + getAlphaFromNum(lastAlphaNum)
    }
}

// 다른 풀이

class Solution {
    fun solution(n: Long, bans: Array<String>): String {
        val bases = bans.map {convertStringToBase26(it)}.sorted()
        var target = n
        
        for(base in bases) {
            if (target >= base) ++target else break
        }
        
        return convertToBase26(target)
    }
    
    private fun convertToBase26(num: Long): String {
        var number = num
        val result = StringBuilder()
        
        while (number-- > 0) {
            val ch = 'a' + (number % 26).toInt()
            result.append(ch)
            number /= 26
        }
        
        return result.reverse().toString()
    }
    
    private fun convertStringToBase26(input: String): Long {
        var result = 0L
        for(char in input) {
            val value = char - 'a' + 1
            result = result * 26 + value
        }
        
        return result
    }
}
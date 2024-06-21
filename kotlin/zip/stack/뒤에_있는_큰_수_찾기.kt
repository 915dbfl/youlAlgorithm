//25분
import kotlin.math.max
import java.util.Stack

class Solution {
    // 스택 + dp
    fun solution(numbers: IntArray): IntArray {
        var answer = IntArray(numbers.size)
        var stack = Stack<Int>()
        var maxValue = 0
        
        // downTo 활용
        for (i in numbers.lastIndex downTo 0) {
            val num = numbers[i]
            // 뒷 큰수가 없는 경우
            if (maxValue <= num) {
                answer[i] = -1
                stack = Stack<Int>()
                stack.push(num)
            } else {
                // num보다 작은 값들 pop하기
                while(stack.isNotEmpty() && stack.last() <= num) {
                    stack.pop()
                }
                answer[i] = stack.last()
                stack.push(num)
            }
            maxValue = max(num, maxValue)
        }
        
        return answer
    }
}

// 조금 더 간단한 풀이
import kotlin.math.max
import java.util.Stack

class Solution {
    fun solution(numbers: IntArray): IntArray {
        var answer = mutableListOf<Int>()
        var stack = Stack<Int>()
        
        for (i in numbers.lastIndex downTo 0) {
            var maxValue = -1
            val num = numbers[i]
            
            while(stack.isNotEmpty()) {
                if(stack.peek() > num) {
                    maxValue = stack.peek()
                    break
                } else {
                    stack.pop()
                }
            }
            
            answer.add(maxValue)
            stack.push(numbers[i])
            
        }
        
        return answer.reversed().toIntArray()
    }
}
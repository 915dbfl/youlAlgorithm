// Int로 answer, n를 다루면 안됨
// Int 범위 최대 21억
import java.io.*
import java.util.*
import kotlin.math.max

fun main() = with(System.`in`.bufferedReader()) {
    val n = readLine().toInt()
    val stack = Stack<Long>()
    
    var answer = 0L
    var num = readLine().toLong()
    var maxNum = num
    stack.push(num)
    repeat(n-1) {
        num = readLine().toLong()
        if (stack.last() < num) {
            answer += num - stack.last()
            maxNum = max(maxNum, num)
        }
        stack.pop()
        stack.push(num)
    }
    answer += maxNum - stack.last()
    print(answer)
}

// 다른 풀이

fun main() = with(System.`in`.bufferedReader()) {
    val n = readLine().toInt()
    val a = mutableListOf<Long>().apply {
        repeat(n) {
            val num = readLine().toLong()
            lastOrNull()?.run {
                if(this != num) 
                    add(num)
            } ?: add(num)
        }
    }

    var answer = 0L
    var maxVal = a.first()
    a.zipWithNext { prev, next ->
        if (prev < next) {
            answer += (next - prev)
        }
        maxVal = maxOf(maxVal, next)
    }
    print(answer + (maxVal - a.last()))
}
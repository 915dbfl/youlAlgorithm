// 오답
import java.io.*
import java.util.*

private var answer = 0

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val n = br.readLine().toInt()
    var nums = arrayListOf<Int>()

    for (i in 0 until n) {
        val tmp = br.readLine().toInt()
        if (nums.isEmpty() || nums.last() != tmp) {
            nums.add(tmp)
        }
    }

    countAdd(nums)
    print(answer)
}

private fun countAdd(nums: MutableList<Int>) {
    val max = nums.indexOf(nums.max())
    
    if (max > 0) {
        val left = nums.subList(0, max)
        val leftMax = left.max()
        answer += nums[max] - leftMax
        countAdd(left)
    }

    if (max < nums.size-1) {
        val right = nums.subList(max+1, nums.size)
        val rightMax = right.max()
        answer += nums[max] - rightMax
        countAdd(right)
    }
}

// 스택 활용
fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val n = br.readLine().toInt()
    var cnt = 0
    val stack = Stack<Int>()

    var num = br.readLine().toInt()
    var maxNum = num
    stack.push(num)

    for (i in 1 until n) {
        num = br.readLine().toInt()
        if (stack.isNotEmpty() && stack.peek() < num) {
            cnt += num - stack.peek()
            maxNum = max(maxNum, num)
        }
        stack.pop()
        stack.push(num)
    }
    if (stack.isNotEmpty()) {
        cnt += maxNum - stack.peek()
    }
    print(cnt)
}
// 메모리 초과
import java.util.StringTokenizer

lateinit var ansSet: MutableSet<String>
lateinit var nums: Set<Char>
var n = 0
var m = 0

fun main() = with(System.`in`.bufferedReader()) {
    val st = StringTokenizer(readLine())
    n = st.nextToken().toInt()
    m = st.nextToken().toInt()
    nums = readLine().split(" ").map {it.single()}.toSet()

    if (n == m) {
        var answer = 1
        for (i in 1..n) {
            answer *= i
        }
        println(answer)
    } else {
        ansSet = mutableSetOf<String>()
        permutation(0, "")
        println(ansSet.size)
    }

}

fun permutation(depth: Int, cur: String) {
    if (depth == n) {
        for (n in nums) {
            if (!cur.contains(n)) {
                return
            }
        }
        ansSet.add(cur)
    } else {
        for (num in 0 until 10) {
            val tmpStr = cur + num.toString()
            permutation(depth+1, tmpStr)
        }
    }
}

import java.util.StringTokenizer

var answer = 0
val toUse = BooleanArray(10)
// 비밀번호 자체를 가지고 있지 않음
// cnt를 통해 선견지명 숫자들이 포함된 갯수만 파악
fun permutation(len: Int, end: Int, m: Int, cnt: Int) {
    if (len == end) {
        if (m == cnt) answer++
        return
    }
    for (i in 0 .. 9) {
        if (toUse[i]) {
            toUse[i] = false
            permutation(len+1, end, m, cnt+1)
            toUse[i] = true
        } else {
            permutation(len+1, end, m, cnt)
        }
    }
}

val br = System.`in`.bufferedReader()
fun main() = with(System.out.bufferedWriter()) {
    val (n, m) = br.readLine().split(" ").map{it.toInt()}
    if (m != 0) {
        val tk = StringTokenizer(br.readLine())
        while(tk.hasMoreTokens()) {
            toUse[tk.nextToken().toInt()] = true
        }
    }

    permutation(0, n, m, 0)
    write("$answer")
    close()
}
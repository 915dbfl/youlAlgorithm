// print 대신 bufferdWriter 사용하기!
// 25분

import java.io.*
import java.util.*

val br = System.`in`.bufferedReader()
fun main() = with(System.out.bufferedWriter()) {
    val n = br.readLine().toInt()
    val levels = br.readLine().split(" ").map {it.toInt()}.toList()
    val pfAccum: IntArray = IntArray(n+1)

    for (i in 1 until n) {
        // 다음 악보보다 어려울 경우 -> 실수를 한다.
        if(levels[i-1] > levels[i]) {
            pfAccum[i] += 1
        }
        pfAccum[i+1] = pfAccum[i]
    }

    val q = br.readLine().toInt()
    repeat(q) {
        val (x, y) = br.readLine().split(" ").map{it.toInt()}
        // 마지막 항목 실수 제외
        write("${pfAccum[y-1] - pfAccum[x-1]}\n")
    } 
    close()
}
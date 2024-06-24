// 오답
import kotlin.collections.ArrayDeque

val br = System.`in`.bufferedReader()
fun main() = with(System.out.bufferedWriter()) {

    var apple = br.readLine().toCharArray()
    var lover = br.readLine().toCharArray()
    val n = apple.size

    apple.sort()
    val appleDq = ArrayDeque<Char>()
    appleDq.addAll(apple.slice(IntRange(0, n - n/2-1)))

    lover.sortDescending()
    val loverDq = ArrayDeque<Char>()
    loverDq.addAll(lover.slice(IntRange(0, n/2-1)))

    var turn = 0
    var idx = 0
    var rev_idx = n-1

    val companyName = Array<Char>(n){' '}

    repeat(n) {
        // 구사과 차례
        if (turn == 0) {
            if (loverDq.isEmpty() || appleDq.first() > loverDq.first()) {
                companyName[rev_idx] = appleDq.removeLast()
                rev_idx--
            } else {
                companyName[idx] = appleDq.removeFirst()
                idx++
            }
        // 러버 차례
        } else {
            if (appleDq.first() > loverDq.first()) {
                companyName[rev_idx] = loverDq.removeLast()
                rev_idx--
            } else {
                companyName[idx] = loverDq.removeFirst()
                idx++
            }
        }
        turn = (turn + 1) % 2
    }
    write("${companyName.joinToString("")}")
    close()

}
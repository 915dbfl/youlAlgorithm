/*
- 문제에서 유성은 무조건 땅보다 위에 존재하기 때문에
다음과 같은 테스트 케이스는 들어오지 않는다.

9 9
.........
..XXXX...
..X......
..X######
..X.....#
..XXXX..#
........#
##.....##
#########

 */

// 오답
import java.util.StringTokenizer

val br = System.`in`.bufferedReader()
val bw = System.out.bufferedWriter()
var r = 0
var s = 0

lateinit var before: Array<CharArray>
lateinit var after: Array<CharArray>

fun findMinDis(): Int {
    var minDis = r+1
    // O(R*S) = 9000000
    // 땅과 유성 거리 중 가장 가까운 거리 구하기
    for (i in 0 until s) {
        var colDis = 0
        for (j in r-2 downTo 0) {
            if (before[j][i] == '.') {
                colDis++
            } else if (before[j][i] == 'X') {
                minDis = minOf(minDis, colDis)
                break
            }
        }
    }
    // println(disDp.joinToString("\n") {it.joinToString()})
    return minDis
}

fun move(moveCnt: Int) {
    after = Array(r) {CharArray(s){'.'}}

    for (i in 0 until r) {
        for (j in 0 until s) {
            when(before[i][j]) {
                'X' -> {
                    after[i+moveCnt][j] = 'X'
                }
                '#' -> after[i][j] = '#'
            }
        }
    }
}

fun main() {
    val st = StringTokenizer(br.readLine())
    r = st.nextToken().toInt()
    s = st.nextToken().toInt()

    before = Array(r) {
        br.readLine().toCharArray()
    }

    val moveCnt = findMinDis()
    move(moveCnt)

    bw.write("${after.joinToString("\n") {it.joinToString("")}}")
    bw.close()
}

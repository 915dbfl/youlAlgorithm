val br = System.`in`.bufferedReader()
val bw = System.out.bufferedWriter()

fun main() {
    val (r, s) = br.readLine().split(" ").map {it.toInt()}
    val before = Array(r) {
        br.readLine().toCharArray()
    }

    // 최대 가능한 이동 거리 구하기
    // 위에서 시작해서 제일먼저 #이 나타나는 곳까지 count해야 함
    /*
    5 2
    X.
    ..
    ##
    .#
    ##
     */
    var moveCnt = r+1
    for (i in 0 until s) {
        var starIdx = -(r+1) // 초기값 설정 주의
        for (j in 0 until r) {
            if (before[j][i] == 'X') starIdx = j
            else if (before[j][i] == '#') { 
                moveCnt = minOf(moveCnt, j - starIdx -1)
                break
            }
        }
    }

    val after = Array(r) {CharArray(s) {'.'}}

    for (i in 0 until r) {
        for (j in 0 until s) {
            when(before[i][j]) {
                'X' -> after[i+moveCnt][j] = 'X'
                '#' -> after[i][j] = '#'
            }
        }
    }

    bw.write("${after.joinToString("\n") {it.joinToString("")}}")
    bw.close()
}
// 헷갈린 부분: 브루트포스를 진행할 때 꼭 상하좌우로 움직이지 않아도 된다.
import java.util.StringTokenizer

val br = System.`in`.bufferedReader()

lateinit var board: Array<IntArray>
val dx = listOf(-1, 1, 0, 0)
val dy = listOf(0, 0, -1, 1)
var answer = -10000
var n = 0
var m = 0
var k = 0

fun canMove(cx: Int, cy: Int, visited: Array<BooleanArray>): Boolean {
    for (i in 0 until 4) {
        val nx = cx + dx[i]
        val ny = cy + dy[i]

        if (0 <= nx && nx < n && 0 <= ny && ny < m) {
            if (visited[nx][ny]) {
                return false
            }
        }
    }
    return true
}

fun recursion(idx: Int, selectedCnt: Int, total: Int, visited: Array<BooleanArray>) {
    if (k == selectedCnt) {
        answer = answer.coerceAtLeast(total)
        return
    }

    if (idx >= n*m) return
    val cx = idx/m
    val cy = idx%m
    val move = canMove(cx, cy, visited)

    if (move) {
        visited[cx][cy] = true
        recursion(idx+1, selectedCnt + 1, total + board[cx][cy], visited)
        visited[cx][cy] = false           
    } 
    recursion(idx+1, selectedCnt, total, visited)

}

fun main() = with(System.out.bufferedWriter()) {
    val st = StringTokenizer(br.readLine())
    n = st.nextToken().toInt()
    m = st.nextToken().toInt()
    k = st.nextToken().toInt()

    board = Array(n) {
        br.readLine().split(" ").map {it.toInt()}.toIntArray()
    }
    val visited = Array(n) { BooleanArray(m) }

    if (n == 1 && m == 1) {
        answer = board.last().last()
    } else{
        recursion(0, 0, 0, visited)
    }
    write("$answer")
    close()
}
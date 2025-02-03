import kotlin.collections.ArrayDeque
import kotlin.math.*

private class Solution17135 {
    // 좌상우
    private val dx = listOf(0, -1, 0)
    private val dy = listOf(-1, 0, 1)

    private fun ArcherCombination(
        m: Int
    ): ArrayList<IntArray> {
        val combis = ArrayList<IntArray>()
        
        for (i in 0 until m) {
            for (j in i+1 until m) {
                for (k in j+1 until m) {
                    combis.add(intArrayOf(i, j, k))
                }
            }
        }

        return combis
    }

    private fun isFinished(
        ax: Int,
        board: Array<IntArray>,
    ): Boolean {
        for (ri in ax-1 downTo 0) {
            if (board[ri].sum() > 0) {
                return false
            }
        }
        return true
    }

    private fun removeEnemy(
        ax: Int,
        ay: Int,
        d: Int,
        board: Array<IntArray>,
    ): Pair<Int, Int>? {
        val dq = ArrayDeque<List<Int>>()
        val visited = Array(board.size) {BooleanArray(board[0].size)}
        // 거리, 현재x, 현재y
        dq.add(listOf(1, ax-1, ay))
        visited[ax-1][ay] = true

        if (board[ax-1][ay] == 1) {
            return ax-1 to ay
        }

        while(dq.isNotEmpty()) {
            val (dist, cx, cy) = dq.removeFirst()

            for (i in 0 until 3) {
                val nx = cx + dx[i]
                val ny = cy + dy[i]

                if (0 <= nx && nx < board.size && 0 <= ny && ny < board[0].size && !visited[nx][ny] && dist + 1 <= d) {
                    if (board[nx][ny] == 1) {
                        return nx to ny
                    }

                    visited[nx][ny] = true
                    dq.add(listOf(dist+1, nx, ny))
                }
            }
        }

        return null
    }

    private fun remove(
        rmSet: Set<Pair<Int, Int>>,
        board: Array<IntArray>,
    ) {
        for((x, y) in rmSet) {
            board[x][y] = 0
        }
    }

    private fun play(
        archers: IntArray,
        d: Int,
        board: Array<IntArray>,
    ): Int {
        // 적이 아닌 궁수가 이동
        var answer = 0
        var removeSet = mutableSetOf<Pair<Int, Int>>()
        for (ax in board.size downTo 0) {
            if (isFinished(ax, board)) break
            for (ai in 0 until 3) {
                val result = removeEnemy(ax, archers[ai], d, board)
                result?.let {
                    removeSet.add(result)
                }
            }
            answer += removeSet.size
            remove(removeSet, board)
            removeSet.clear()
        }
        return answer
    }

    fun solve(
        n: Int,
        m: Int, 
        d: Int,
        board: Array<IntArray>,
    ) {
        val archerCombination = ArcherCombination(m)
        var answer = 0
        for (archers in archerCombination) {
            val newBoard = board.map {it.copyOf()}.toTypedArray()
            answer = max(answer, play(archers, d, newBoard))
        }
        println(answer)
    }
}

fun main() = with(System.`in`.bufferedReader()) {
    val (n, m, d) = readLine().split(" ").map {it.toInt()}
    val board = Array(n) {
        readLine().split(" ").map {it.toInt()}.toIntArray()
    }
    Solution17135().solve(n, m, d, board)
}
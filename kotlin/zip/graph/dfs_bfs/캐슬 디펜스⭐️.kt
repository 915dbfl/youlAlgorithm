// 1시간 10분
import kotlin.math.*
import java.util.ArrayDeque

private class Solution17135(
    private val n: Int,
    private val m: Int, 
    private val d: Int,
    private val board: Array<IntArray>,
) {
    private var maxRm = 0
    private val dx = listOf(0, -1, 0)
    private val dy = listOf(-1, 0, 1)
    private lateinit var tempBoard: Array<IntArray>

    fun solve(): Int {
        // 조합 구하기
        for (i in 0 until m) {
            for (j in i+1 until m) {
                for (k in j+1 until m) {
                    tempBoard = Array(n) {board[it].copyOf()}
                    play(n, i, j, k, 0)
                }
            }
        }

        return maxRm
    }

    private fun play(start: Int, first: Int, second: Int, third:Int, totalRm: Int) {
        if (start == 0 || removeAllEnemy(start)) {
            maxRm = max(maxRm, totalRm)
            return
        }
        
        val enemies = mutableSetOf<Pair<Int, Int>>()
        findEnemy(start, first)?.let{ enemies.add(it) }
        findEnemy(start, second)?.let{ enemies.add(it) }
        findEnemy(start, third)?.let{ enemies.add(it) }

        // 적 제거
        for((x, y) in enemies) {
            tempBoard[x][y] = 0
        }

        play(start - 1, first, second, third, totalRm + enemies.size)
    }

    private fun removeAllEnemy(start: Int): Boolean {
        for (i in start - 1 downTo 0) {
            if (tempBoard[i].sum() > 0) {
                return false
            }
        }
        return true
    }

    // dfs
    private fun findEnemy(x: Int, y: Int): Pair<Int, Int>? {
        val dq = ArrayDeque<Pair<Int, Int>>()
        val visited = Array(n) {BooleanArray(m)}
        dq.add(x-1 to y)
        visited[x-1][y] = true

        while (dq.isNotEmpty()) {
            val (curx, cury) = dq.removeFirst()

            if (tempBoard[curx][cury] == 1) {
                return curx to cury
            }

            for (i in 0 until 3) {
                val nx = curx + dx[i]
                val ny = cury + dy[i]

                if (0 <= nx && 0 <= ny && ny < m &&  calDist(x, y, nx, ny) <= d && !visited[nx][ny]) {
                    visited[nx][ny] = true
                    dq.add(nx to ny)
                }
            }
        }

        return null
    }

    private fun calDist(x: Int, y: Int, nx: Int, ny: Int): Int {
        return abs(nx - x) + abs(ny - y)
    }
}

fun main() = with(System.`in`.bufferedReader()) {
    val (n, m, d) = readLine().split(" ").map {it.toInt()}
    val board = Array(n) {
        readLine().split(" ").map {it.toInt()}.toIntArray()
    }
    val solution17135 = Solution17135(n, m, d, board)
    println(solution17135.solve())
}
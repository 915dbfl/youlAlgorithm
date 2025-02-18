// 재귀 / 게임 이론

import kotlin.math.*

private class Solution16571(
    private val board: Array<IntArray>,
) {
    private val cnts = IntArray(3)
    private val LOSE = 0
    private val DRAW = 1

    private fun play(turn: Int): Int {
        if (isFinished(turn)) {
            return 0 // 이전 선수가 이미 이긴 경우, 지게 됨
        }

        var min_result = 3
        for (i in 0 until 3) {
            for (j in 0 until 3) {
                if (board[i][j] == 0) {
                    board[i][j] = turn
                    min_result = min(min_result, play((turn % 2) + 1))
                    board[i][j] = 0
                }
            }
        }

        return when(min_result) {
            0 -> 2
            1, 3 -> 1
            else -> 0
        }
    }

    fun solve(): Char {
        val turn = searchStart()
        if (cnts[0] == 0) {
            return 'D'
        } else {
            val result = play(turn)
            return when(result) {
                LOSE -> 'L'
                DRAW -> 'D'
                else -> 'W'
            }
        }
    }

    private fun searchStart(): Int {
        for (i in 0 until 3) {
            for (j in 0 until 3) {
                cnts[board[i][j]] += 1
            }
        }

        return if (cnts[1] == cnts[2]) 1 else 2
    }

    private fun isFinished(turn: Int): Boolean {
        val nxtTurn = (turn % 2) + 1
        // 대각선 확인 
        if ((board[0][0] == board[1][1] && board[1][1] == board[2][2] && board[2][2] == nxtTurn) || (board[0][2] == board[1][1] && board[1][1] == board[2][0] && board[2][0] == nxtTurn)) {
            return true
        }
        // 가로 세로 확인
        for (i in 0 until 3) {
            if ((board[i][0] == board[i][1] && board[i][1] == board[i][2] && board[i][2] == nxtTurn) || (board[0][i] == board[1][i] && board[1][i] == board[2][i] && board[2][i] == nxtTurn)) {
                return true
            }
        }

        return false
    }
}

fun main() = with(System.`in`.bufferedReader()) {
    val board = Array(3) {
        readLine().split(" ").map {it.toInt()}.toIntArray()
    }

    val solution16571 = Solution16571(board)
    println(solution16571.solve())
}
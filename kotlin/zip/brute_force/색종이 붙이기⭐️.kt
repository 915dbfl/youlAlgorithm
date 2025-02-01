/*
풀이 과정 - 재귀
 */

import kotlin.math.*

private class Solution17136(
    val paper: Array<IntArray>
) {
    private val paperSize = IntArray(5) {5}
    private val visited = Array(10) {BooleanArray(10)}
    private var answer = Int.MAX_VALUE

    private fun checkSize(
        x: Int,
        y: Int,
        size: Int
    ): Boolean {
        for (i in 0 until size) {
            for (j in 0 until size) {
                if (x + i >= 10 || y + j >= 10 || paper[x+i][y+j] == 0 || visited[x+i][y+j]) {
                    return false
                }
            }
        }
        return true
    }

    private fun setVisited(
        x: Int,
        y: Int,
        size: Int,
        value: Boolean
    ) {
        for (i in 0 until size) {
            for (j in 0 until size) {
                visited[x+i][y+j] = value
            }
        }
    }

    private fun checkPaper(cnt: Int): Int {
        // 가지치기
        if (cnt >= answer) {
            return answer
        }

        var sx = -1
        var sy = -1

        for (i in 0 until 10) {
            for (j in 0 until 10) {
                if (paper[i][j] == 1 && !visited[i][j]) {
                    sx = i
                    sy = j
                    break
                }
            }
            if (sx != -1) break
        }

        if (sx == -1) {
            return cnt
        }

        for (k in 5 downTo 1) {
            if (sx + k - 1 < 10 && sy + k - 1 < 10) {
                // 해당 사이즈 종이를 사용할 수 있는 경우
                if (checkSize(sx, sy, k) && paperSize[k-1] > 0) {
                    // visited 셋팅
                    setVisited(sx, sy, k, true)
                    paperSize[k-1] -= 1
                    val result = checkPaper(cnt+1)
                    answer = min(answer, result)
                    // visited 풀기
                    paperSize[k-1] += 1
                    setVisited(sx, sy, k, false)
                }
            }
        }

        return answer
    }

    fun solve(): Int {
        val result = checkPaper(0)
        return if (result == Int.MAX_VALUE) -1 else result
    }
}

fun main() = with(System.`in`.bufferedReader()) {
    val paper = Array(10) {
        readLine().split(" ").map {it.toInt()}.toIntArray()
    }

    println(Solution17136(paper).solve())
}
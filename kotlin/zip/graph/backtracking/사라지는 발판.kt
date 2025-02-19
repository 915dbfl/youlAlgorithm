import kotlin.math.*

class Solution {
    private val dx = listOf(-1, 1, 0, 0)
    private val dy = listOf(0, 0, -1, 1)
    private lateinit var playBoard: Array<IntArray>
    
    private fun play(curx: Int, cury: Int, nx: Int, ny: Int): Pair<Boolean, Int> {
        // 움직일 곳이 없어 게임이 끝난 경우
        if (isFinished(curx, cury)) {
            return false to 0
        }
        
        // 동일한 곳에 서 있을 경우, 현재 플레이어가 움직이면 게임이 끝남
        if (curx == nx && cury == ny) {
            return true to 1
        }
        
        var winMin = Int.MAX_VALUE
        var loseMax = 0
        
        for (i in 0 until 4) {
            val nxtX = curx + dx[i]
            val nxtY = cury + dy[i]
            
            if (inRange(nxtX, nxtY) && playBoard[nxtX][nxtY] == 1) {
                playBoard[curx][cury] = 0
                val result = play(nx, ny, nxtX, nxtY)
                if (!result.first) {
                    // 이기는 상황에서는 최대한 빨리 이길 수 있는 경우 기록
                    winMin = min(winMin, result.second + 1)
                } else {
                    // 지는 상황에서는 최대한 오래 버틸 수 있는 경우 기록
                    loseMax = max(loseMax, result.second + 1)
                }
                playBoard[curx][cury] = 1
            }
        }
        
        // 이기는 경우가 존재한다면 -> 최적의 플레이로 이기는 플레이 진행
        if(winMin != Int.MAX_VALUE) {
            return true to winMin
        } else {
            return false to loseMax
        }
    }
    
    fun isFinished(curx: Int, cury: Int): Boolean {
        for (i in 0 until 4) {
            val nxtX = curx + dx[i]
            val nxtY = cury + dy[i]
            
            // 움직일 곳이 하나라도 있을 경우
            if (inRange(nxtX, nxtY)) {
                if (playBoard[nxtX][nxtY] == 1) {
                    return false
                }
            }
        }
        return true
    }
    
    private fun inRange(x: Int, y: Int): Boolean {
        return (0 <= x && x < playBoard.size && 0 <= y && y < playBoard[0].size)
    }
    
    fun solution(board: Array<IntArray>, aloc: IntArray, bloc: IntArray): Int {
        playBoard = board
        return (play(aloc[0], aloc[1], bloc[0], bloc[1])).second
    }
}
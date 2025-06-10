/*
해설
1. (n+2) * (m+2) 크기의 보드 생성
    - 테두리는 모두 외부로 처리 -> visited 표시
2. 직접 제거한 컨테이너 처리
    - 단순 visited로 표시
3. bfs 처리
    - 0,0 외부에서 시작해 bfs 진행
    - 처음 방문하고 타겟이라면 -> visited 설정
    - visited 컨테이너일 경우 외부로 처리 -> 큐에 삽입
        - visited 컨테이너의 경우 주변을 확인해야 하기 떄문에 visited와 별개로 memo 기록
*/

import java.util.*

class Solution {    
    private var N = 0
    private var M = 0
    private val dx = intArrayOf(-1, 0, 1, 0)
    private val dy = intArrayOf(0, 1, 0, -1)

    private lateinit var board : Array<CharArray>

    private data class Coordinate(val x : Int, val y : Int) 
    
    fun solution(storage: Array<String>, requests: Array<String>): Int {
        var answer: Int = 0
        
        N = storage.size + 2
        M = storage[0].length + 2
        board = Array(N) { i->
            CharArray(M) { j ->
                if(i in 1 until N - 1 && j in 1 until M - 1) {
                    storage[i - 1][j - 1]
                } else {
                    ' '
                }
            }
        }

        // 방문 초기화
        val isVisited = Array(N) { BooleanArray(M) }
        initVisited(isVisited)

        // 명령 처리
        for(request in requests) {
            val target = request[0]
            
            // 외부와 연결된 노드 bfs로 방문 처리
            if(request.length == 1) {
                BFS(target, isVisited)            
            } else {
                // 외부와 연결되지 않은 노드는 직접 방문 처리
                for(j in 1..N - 1) {
                    for(k in 1..M - 1) {
                        if(!isVisited[j][k] && board[j][k] == target) {
                            isVisited[j][k] = true
                        }
                    }
                }
            }
        }
        
        // 방문하지 않은 노드만 count
        var ans = 0
        for(i in 1 until N-1) {
            for(j in 1 until M-1) {
                if(!isVisited[i][j]) ans++
            }
        }
        
        return ans
    }

    private fun initVisited(visited: Array<BooleanArray>) {
        for(i in 0 until N) {
            for(j in 0 until M) {
                if(i == 0 || i == N - 1) {
                    isVisited[i][j] = true
                } else if(j == 0 || j == M - 1) {
                    isVisited[i][j] = true
                }
            }
        }
    }
    
    private fun BFS(target : Char, isVisited : Array<BooleanArray>) {
        val que = ArrayDeque<Coordinate>()
        val memo = Array(N) { BooleanArray(M)}
        que.push(Coordinate(0, 0))
        memo[0][0] = true
        
        while(que.isNotEmpty()) {
            val cur = que.pop()
            
            for(i in 0 until 4) {
                val nX = dx[i] + cur.x
                val nY = dy[i] + cur.y
                
                if(!check(nX, nY, memo)) continue
                
                // 이미 직접 제거된 경우 -> 외부로 처리
                if(isVisited[nX][nY]) {
                    que.addLast(Coordinate(nX, nY))
                    memo[nX][nY] = true
                // 그게 아니라면 방문 처리
                } else if(!isVisited[nX][nY] && board[nX][nY] == target) {
                    isVisited[nX][nY] = true
                    memo[nX][nY] = true
                }
            }
        }
    }
    
    private fun check(x : Int, y : Int, memo : Array<BooleanArray>) : Boolean {
        return x in 0 until N && y in 0 until M && !memo[x][y]
    }
}
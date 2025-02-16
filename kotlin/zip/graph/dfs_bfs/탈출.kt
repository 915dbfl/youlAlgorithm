// 1시간 14분
/*
주요 정보
1. 물이 있는 칸과 인접한 비어있는 칸은 물이 찬다.
2. 물 / 고슴도치 모두 돌을 통과할 수 없다.
3. 고슴도치는 물이 차 있는 곳으로 이동할 수 없다.
4. 물은 비버의 소굴로 이동할 수 없다.
5. 다음에 물이 찰 지역으로 고슴도치는 이동할 수 없다.

풀이 과정 - bfs
1. 고슴도치 위치 파악
2. 물 위치 파악 (4면 중 한 면이라도 .와 인접한 경우)
3. bfs 진행
    - 다음의 과정 반복
        - 물 이동
        - 고슴도치 이동
            : 이동한 곳의 4면 중 한 면이라도 물이 있는 경우 이동 불가
            : 가능한 모든 이동 dq에 저장
 */

import java.util.ArrayDeque

private class Solution3055(
    private val r: Int,
    private val c: Int,
    private val graph: Array<CharArray>,
) {
    private var hedgehog = ArrayDeque<Pair<Int, Int>>()
    private var water = ArrayDeque<Pair<Int, Int>>()
    val visited = Array(r) {IntArray(c) {-1}}

    private val dx = listOf(-1, 1, 0, 0)
    private val dy = listOf(0, 0, -1, 1)
    private var answer = -1

    private fun init() {
        for (i in 0 until r) {
            for (j in 0 until c) {
                if (graph[i][j] == '*') {
                    water.offer(i to j)
                }
                else if (graph[i][j] == 'S') {
                    graph[i][j] = '.'
                    hedgehog.offer(i to j)
                    visited[i][j] = 0
                }
            }
        }
    }

    private fun isNear(x: Int, y: Int, target: Char): Boolean {
        for (i in 0 until 4) {
            val nx = x + dx[i]
            val ny = y + dy[i]

            if ((nx in 0 until r) && (ny in 0 until c) && graph[nx][ny] == target) {
                return true
            }
        }
        return false
    }

    private fun move() {
        while(hedgehog.isNotEmpty()) {
            // 고슴도치 이동
            repeat(hedgehog.size) {
                val (hx, hy) = hedgehog.poll()
                for (i in 0 until 4) {
                    val nx = hx + dx[i]
                    val ny = hy + dy[i]

                    // 범위 내 && 비어있는 공간 && 방문하지 않은 곳 && 다음에 물이 안 차는 공간
                    if ((nx in 0 until r) && (ny in 0 until c)) {
                        if (graph[nx][ny] == 'D' ) {
                            answer = visited[hx][hy] + 1
                            return
                        } else if (graph[nx][ny] == '.' && (visited[nx][ny] == -1) && !isNear(nx, ny, '*')) {
                            hedgehog.offer(nx to ny)
                            visited[nx][ny] = visited[hx][hy] + 1
                        }
                    }
                }
            }

            // 물 이동
            repeat(water.size) {
                val (wx, wy) = water.poll()
                for (i in 0 until 4) {
                    val nx = wx + dx[i]
                    val ny = wy + dy[i]

                    // 범위 내 && 비어있는 공간 -> 물 채우기
                    if ((nx in 0 until r) && (ny in 0 until c) && graph[nx][ny] == '.') {
                        water.offer(nx to ny)
                        graph[nx][ny] = '*'
                    }
                }
            }
        }
    }
    
    fun solve(): String {
        init()
        move()
        return if (answer != -1) answer.toString() else "KAKTUS"
    }
}

fun main() = with(System.`in`.bufferedReader()) {
    val (r, c) = readLine().split(" ").map {it.toInt()}
    val graph = Array(r) {
        readLine().toCharArray()
    }

    val solution3055 = Solution3055(r, c, graph)
    println(solution3055.solve())
}
/*
풀이 과정
알고리즘: brute force + backTracking
1. 이동 상하좌우(거울은 비스듬히 설치되기 때문에 대각선을 고려하지 않음)
2. 이동한 위치에 거울이 있다면 갈 수 있는 방향이 각각 두 가지
3. 또 다른 거울을 만나면 설치한 거울 수 최소값으로 업데이트
4. visited를 통해 방문한 위치 기록 (거울 반사 방문 / 일반 방문 분리)
 */

private class Solution2151(
    private val n: Int,
    private val room:Array<CharArray>,
) {
    private val mirror = ArrayList<Pair<Int, Int>>()
    private val visited = Array(n){Array(n){IntArray(4){-1}}}
    private val dx = listOf(-1, 1, 0, 0)
    private val dy = listOf(0, 0, -1, 1)

    init {
        // 거울 위치 구하기
        for (i in 0 until n) {
            for (j in 0 until n) {
                if (room[i][j] == '#') {
                    mirror.add(i to j)
                }
            }
        }
    }

    fun solve(): Int {
        val dq = ArrayDeque<Triple<Int, Int, Int>>()
        val (start, end) = mirror
        for (i in 0..3) {
            visited[start.first][start.second][i] = 0
            dq.add(Triple(start.first, start.second, i))
        }

        while (dq.isNotEmpty()) {
            val (curX, curY, curDir) = dq.removeFirst()
            if (curX == end.first && curY == end.second) {
                return visited[curX][curY][curDir]
            }

            val nx = curX + dx[curDir]
            val ny = curY + dy[curDir]

            if (nx < 0 || nx >= n || ny < 0 || ny >= n) continue
            if (room[nx][ny] == '*') continue

            if (visited[nx][ny][curDir] == -1 || visited[nx][ny][curDir] > visited[curX][curY][curDir]) {
                visited[nx][ny][curDir] = visited[curX][curY][curDir]
                dq.addFirst(Triple(nx, ny, curDir))
            }

            if (room[nx][ny] == '!') {
                val nd = if (curDir in setOf(0, 1)) listOf(2, 3) else listOf(0, 1)
                for (newDir in nd) {
                    if (visited[nx][ny][newDir] == -1 || visited[nx][ny][newDir] > (visited[curX][curY][curDir] + 1)) {
                        visited[nx][ny][newDir] = visited[curX][curY][curDir] + 1
                        dq.addLast(Triple(nx, ny, newDir))
                    }
                }
            }
        }

        return -1
    }
}

fun main() = with(System.`in`.bufferedReader()) {
    val n = readLine().toInt()
    val room = Array(n) {readLine().toCharArray()}
    val solution2151 = Solution2151(n, room)
    println(solution2151.solve())
}
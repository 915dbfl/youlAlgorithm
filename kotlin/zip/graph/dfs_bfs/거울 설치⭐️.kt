fun main() = with(System.`in`.bufferedReader()) {
    val n = readLine().toInt()
    val rooms = Array(n) {readLine().toCharArray()}
    val visited = Array(n) {Array(n) { intArrayOf(-1, -1, -1, -1)}}

    var start = -1 to -1
    var end = -1 to -1

    for (i in 0..<n) {
        for (j in 0..<n) {
            if (rooms[i][j] =='#') {
                if (start.first == -1 && start.second == -1) {
                    start = i to j
                } else {
                    end = i to j
                }
            }
        }
    }

    val dx = listOf(-1, 1, 0, 0)
    val dy = listOf(0, 0, -1, 1)

    val dq = ArrayDeque<Triple<Int, Int, Int>>()
    for (i in 0..3) {
        visited[start.first][start.second][i] = 0
        dq.add(Triple(start.first, start.second, i))
    }

    while(dq.isNotEmpty()) {
        val (curX, curY, curDir) = dq.removeFirst()
        if (curX == end.first && curY == end.second) {
            print(visited[curX][curY][curDir])
            break
        }

        val nx = curX + dx[curDir]
        val ny = curY + dy[curDir]

        if (nx < 0 || nx >= n || ny < 0 || ny >= n) continue
        if (rooms[nx][ny] == '*') continue

        if (visited[nx][ny][curDir] == -1 || visited[nx][ny][curDir] > visited[curX][curY][curDir]) {
            visited[nx][ny][curDir] = visited[curX][curY][curDir]
            dq.addFirst(Triple(nx, ny, curDir))
        }
        if (rooms[nx][ny] == '!') {
            val nd = if (curDir in setOf(0, 1)) listOf(2, 3) else listOf(0, 1)
            for (newDir in nd) {
                if (visited[nx][ny][newDir] == -1 || visited[nx][ny][newDir] > visited[curX][curY][curDir] + 1) {
                    visited[nx][ny][newDir] = visited[curX][curY][curDir] + 1
                    dq.addLast(Triple(nx, ny, newDir))
                }
            }
        }
    }
}
// 1시간 30분
val bw = System.out.bufferedWriter()

lateinit var result: CharArray
lateinit var gameBoard: Array<CharArray>
var unkownRow = 0
var k = 0
lateinit var beforeQResult: CharArray
lateinit var afterQResult: CharArray

const val BASE_CH = 'A'
const val LADDER_CH = '-'
const val NO_LADDER_CH = '*'
const val CROSS_CH = "x"

fun main() = with(System.`in`.bufferedReader()) {
    k = readLine().toInt()
    val n = readLine().toInt()

    // 사다리 및 결과 입력받기
    result = readLine().toCharArray()
    gameBoard = Array(n) {
        val row = readLine().toCharArray()
        if (row[0] == '?') unkownRow = it
        row
    }

    // 사다리 끊기기 전 결과 구하기
    val player = CharArray(k) { BASE_CH + it }
    if (unkownRow == 0) {
        beforeQResult = player
        afterQResult = playLadderGame(result, gameBoard.slice(unkownRow+1..gameBoard.size-1).reversed())
    } else if (unkownRow == n-1) {
        beforeQResult = playLadderGame(player, gameBoard.slice(0..unkownRow-1))
        afterQResult = result
    } else {
        beforeQResult = playLadderGame(player, gameBoard.slice(0..unkownRow-1))
        afterQResult = playLadderGame(result, gameBoard.slice(unkownRow+1..gameBoard.size-1).reversed())
    }

    bw.write("${getQLadder(beforeQResult, afterQResult)}")
    bw.close()
}

fun getQLadder(array1: CharArray, array2: CharArray): String {
    var answer = ""
    var idx = 0
    
    while (idx < k-1) {
        if (array1[idx] == array2[idx]) {
            answer += NO_LADDER_CH
        } else if (array1[idx] == array2[idx+1]) {
            answer += LADDER_CH
            answer += NO_LADDER_CH
            idx += 1
        } else {
            return CROSS_CH.repeat(k-1)
        }
        idx += 1
    }

    return answer.slice(0..k-2)
}

fun playLadderGame(player: CharArray, gameBoard: List<CharArray>): CharArray {
    val gameResult = Array(gameBoard.size+1) {CharArray(k)}


    // 초기 위치 배정
    repeat(k) {
        gameResult[0][it] = player[it]
    }

    for (i in 0 until gameBoard.size) {
        // 첫번째 위치 처리
        if (gameBoard[i][0] == LADDER_CH) {
            gameResult[i+1][1] = gameResult[i][0]
        } else {
            gameResult[i+1][0] = gameResult[i][0]
        }

        // 마지막 위치 처리
        if(gameBoard[i].last() == LADDER_CH) {
            gameResult[i+1][k-2] = gameResult[i][k-1]
        } else {
            gameResult[i+1][k-1] = gameResult[i][k-1]
        }
        
        for (j in 1 until k-1) {
            // 왼쪽에 사다리가 있는 경우
            if (gameBoard[i][j-1] == LADDER_CH) {
                gameResult[i+1][j-1] = gameResult[i][j]
            } else if (gameBoard[i][j] == LADDER_CH) {
                gameResult[i+1][j+1] = gameResult[i][j]
            } else {
                gameResult[i+1][j] = gameResult[i][j]
            }
        }
    }

    // println(gameResult.joinToString("\n") {it.joinToString()})
    return gameResult.last()
}

// 다른 풀이
fun main() {
    val (k, n) = readLine()!!.toInt() to readLine()!!.toInt()
    var blankIdx = 0
    val up = CharArray(k) { 'A' + it }
    val down = readLine()!!.toCharArray()
    val ans = CharArray(k-1) {'*'}

    val cmds = Array(n) {
        val cmd = readLine()!!.toCharArray()
        if (cmd[0] == '?') blankIdx = it
        cmd
    }

    for (i in 0 until blankIdx) {
        val cmd = cmds[i]
        cmd.forEachIndexed {idx, value -> 
            if (value == '-') {
                swap(idx, idx+1, up)
            }
        }
    }

    for (i in n-1 downTo blankIdx+1) {
        val cmd = cmds[i]
        cmd.forEachIndexed {idx, value ->
            if (value == '-') {
                swap(idx, idx+1, down)
            }
        }
    }

    for(i in 0 until k-1) {
        if (up[i] != down[i]) {
            if (up[i] == down[i+1] && up[i+1] == down[i]) {
                ans[i] = '-'
            } else {
                if (i == 0 || ans[i-1] != '-') {
                    for (j in ans.indices) {
                        ans[j] = 'x'
                    }
                    break
                }
            }
        }
    }

    println(ans.joinToString(""))
}

private fun swap(i: Int, j: Int, arr: CharArray) {
    val temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
}

// 재풀이
// 1시간 반

fun main() = with(System.`in`.bufferedReader()) {
    val k = readLine().toInt()
    val n = readLine().toInt()

    val order = readLine().toCharArray()
    val lines = arrayListOf<CharArray>()
    var unknown = -1

    fun downPlay(start: CharArray, s: Int, e: Int): CharArray {
        val result = CharArray(k){' '}
        // 알파벳 이동
        for (i in 0 until k) {
            var cur = i
            for (j in s until e) {
                if (cur < k-1 && lines[j][cur] == '-') {
                    cur += 1
                } else if (cur > 0 && lines[j][cur-1] == '-' ) {
                    cur -= 1
                }
            }
            result[cur] = start[i]
        }
        return result
    }

    fun upPlay(start: CharArray, s: Int, e: Int): CharArray {
        val result = CharArray(k){' '}
        // 알파벳 이동
        for (i in 0 until k) {
            var cur = i
            for (j in s downTo e) {
                if (cur < k-1 && lines[j][cur] == '-') {
                    cur += 1
                } else if (cur > 0 && lines[j][cur-1] == '-' ) {
                    cur -= 1
                }
            }
            result[cur] = start[i]
        }
        return result
    }

    for (i in 0 until n) {
        val line = readLine().toCharArray()
        if (line[0] == '?') {
            unknown = i
        }

        lines.add(line)
    }

    val start = CharArray(k) {'A' + it}
    val topResult = downPlay(start, 0, unknown)
    val bottomResult = upPlay(order, n-1, unknown+1)

    val answer = StringBuilder()
    for (i in 0 until k-1) {
        if (topResult[i] == bottomResult[i] || (i > 0 && topResult[i] == bottomResult[i-1])) {
            answer.append("*")
        } else if (topResult[i] == bottomResult[i+1]) {
            answer.append("-")
        } else {
            print("x".repeat(k-1))
            return
        }
    }
    print(answer.toString())
}
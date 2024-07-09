/*
다음의 경우도 생각하기!

11111(비교대상)
10000
11111
10000
11111
    11111(기준)
    10000
    11111
    10000
    11111
 */
fun rotate(base: Array<CharArray>): Array<CharArray> {
    val baseRow = base.size
    val baseCol = base.first().size

    val result = Array(baseCol) {CharArray(baseRow)}
    for (row in 0 until baseRow) {
        for (col in 0 until baseCol) {
            result[col][row] = base[baseRow-1-row][col]
        }
    }
    
    return result
}

fun main() = with(System.`in`.bufferedReader()) {
    val (n1, m1) = readLine().split(" ").map {it.toInt()}
    val puzzle1 = Array(n1) {
        readLine().map{it}.toCharArray()
    }

    val (n2, m2) = readLine().split(" ").map {it.toInt()}
    val puzzle2 = Array(n2) {
        readLine().map{it}.toCharArray()
    }

    println("${getMinFrame(puzzle1, puzzle2)}")
}

fun getMinFrame(p1: Array<CharArray>, p2: Array<CharArray>): Int {
    var puzzle1 = p1

    var minFrame = 10001

    val p2Row = p2.size
    val p2Col = p2.first().size

    repeat(4) {
        for (i in -p2Row until puzzle1.size) {
            for (j in -p2Col until puzzle1.first().size) {
                if (checkOk(i, j, puzzle1, p2)) {
                    var height = 0; var width = 0;
                    if (i < 0) {
                        height = maxOf(p2Row, -i + puzzle1.size)
                    } else {
                        height = maxOf(i+p2Row, puzzle1.size)
                    }
                    
                    if (j < 0) {
                        width = maxOf(p2Col, -j + puzzle1.first().size)
                    } else {
                        width = maxOf(j+p2Col, puzzle1.first().size)
                    }

                    minFrame = minOf(minFrame, height*width)
                }
            }
        }
        puzzle1 = rotate(puzzle1)
    }

    return minFrame
}

fun checkOk(sx: Int, sy: Int, p1: Array<CharArray>, p2: Array<CharArray>): Boolean {
    for (i in 0 until p2.size) {
        for (j in 0 until p2.first().size) {
            val nx = sx + i; val ny = sy + j
            if (0 <= nx && nx < p1.size && 0 <= ny && ny < p1.first().size) {
                if (p1[nx][ny] == '1' && p2[i][j] == '1') {
                    return false
                }
            }
        }
    }
    return true
}
// 단순 구현
// 30분
val bw = System.out.bufferedWriter()

const val SEAT_NUM = 20

fun main() = with(System.`in`.bufferedReader()) {
    val (n, m) = readLine().split(" ").map {it.toInt()}
    val orders = Array(m) {
        readLine().split(" ").map {it.toInt()}
    }

    val trains = Array(n+1) {
        MutableList(SEAT_NUM){0}
    }

    // 명령 처리
    for (order in orders) {
        when(order[0]) {
            1 -> {
                if (trains[order[1]][order[2]-1] == 0) {
                    trains[order[1]][order[2]-1]++
                }
            }
            2 -> {
                if (trains[order[1]][order[2]-1] == 1) {
                    trains[order[1]][order[2]-1]--
                }
            }
            3 -> {
                trains[order[1]].removeAt(SEAT_NUM-1)
                trains[order[1]].add(0, 0)
            }
            else -> {
                trains[order[1]].removeAt(0)
                trains[order[1]].add(0)
            }
        }
        // println("중간 점검")
        // println(trains.joinToString("\n") {it.joinToString()})
    }

    val answer = mutableSetOf<String>()
    for (i in 1 until n+1) {
        val trainStr = trains[i].joinToString()
        answer.add(trainStr)
    }

    bw.write("${answer.size}")
    bw.close()
}

// 비트마스킹

fun main() = with(System.`in`.bufferedReader()) {
    val (n, m) = readLine().split(" ").map {it.toInt()}
    val train = Array(n) {0}
    val maxBit = (1 shl 20) - 1

    (1..m).forEach {_ ->
        val op = readLine().split(" ")
        // op가 empty면 NoSuchElementException 발생
        val opNum = op[0].toInt()
        val tNum = op[1].toInt() - 1

        when(opNum) {
            1-> {
                op.getOrNull(2)?.let {
                    val seat = it.toInt()
                    train[tNum] = train[tNum] or (1 shl (seat - 1))
                }
            }
            2 -> {
                op.getOrNull(2)?.let {
                    val seat = it.toInt()
                    // inv로 비트 반전
                    train[tNum] = train[tNum] and (1 shl (seat - 1)).inv()
                }
            }
            3 -> {
                train[tNum] = train[tNum] shl 1
                train[tNum] = train[tNum] and maxBit
            }
            4 -> train[tNum] = train[tNum] shr 1
        }
    }

    println(train.toSet().size)
}
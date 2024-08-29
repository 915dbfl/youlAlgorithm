package kr.co.fastcampus.part4plus.baseracegame.feature.game

fun main() = with(System.`in`.bufferedReader()) {
    var wheelStateList = mutableListOf<List<Int>>()
    val scoreList = listOf(1, 2, 4, 8)
    repeat(4) {
        wheelStateList.add(readLine().map { it.toString().toInt() })
    }

    val spinCnt = readLine().toInt()
    repeat(spinCnt) {
        val (wheeIdx, direction) = readLine().split(" ").map {it.toInt()}
        val dirList = getDirection(wheeIdx, direction, wheelStateList)
        wheelStateList = processSpin(dirList, wheelStateList)
    }

    println(getScore(wheelStateList, scoreList))
}

private fun getScore(wheelStateList: List<List<Int>>, scoreList: List<Int>) = wheelStateList.foldIndexed(0) { idx, total, list ->
    val score = if (list[0] == 1) scoreList[idx] else 0
    total + score
}

private fun getDirection(
    wheelIdx: Int,
    direction: Int,
    wheelStateList: MutableList<List<Int>>
): List<Int> {
    val dirList = mutableListOf(0, 0, 0, 0)
    dirList[wheelIdx - 1] = direction

    // 오른쪽 바퀴 처리
    for (i in 0 until (4 - wheelIdx)) {
        // 반대 방향으로 회전
        if (wheelStateList[wheelIdx + i - 1][CHECK_RIGHT_IDX] != wheelStateList[wheelIdx + i][CHECK_LEFT_IDX]) {
            dirList[wheelIdx + i] = -dirList[wheelIdx + i - 1]
        } else {
            break
        }
    }

    // 왼쪽 바퀴 처리
    for (i in 0 until wheelIdx - 1) {
        // 반대 방향으로 회전
        if (wheelStateList[wheelIdx - i - 1][CHECK_LEFT_IDX] != wheelStateList[wheelIdx - i - 2][CHECK_RIGHT_IDX]) {
            dirList[wheelIdx - i - 2] = -dirList[wheelIdx - i - 1]
        } else {
            break
        }
    }

    return dirList
}

private fun processSpin(
    dirList: List<Int>,
    wheelStateList: MutableList<List<Int>>
): MutableList<List<Int>> {
    val newWheelStateList = mutableListOf<List<Int>>()
    wheelStateList.forEachIndexed { index, wheelState ->
        val newList = mutableListOf<Int>()
        if (dirList[index] == 1) {
            newList.add(wheelState.last())
            newList.addAll(wheelState.dropLast(1))
            newWheelStateList.add(newList)
        } else if (dirList[index] == -1) {
            newList.addAll(wheelState.drop(1))
            newList.add(wheelState.first())
            newWheelStateList.add(newList)
        } else {
            newWheelStateList.add(wheelState)
        }
    }
    return newWheelStateList
}

const val CHECK_RIGHT_IDX = 2
const val CHECK_LEFT_IDX = 6
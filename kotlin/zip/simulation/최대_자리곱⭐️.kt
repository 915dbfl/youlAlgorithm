val bw = System.out.bufferedWriter()

fun main() = with(System.`in`.bufferedReader()) {
    val numStr = readLine().toString()

    var answer = calc(numStr)
    val tmpNumList = CharArray(numStr.length){'0'}
    for(i in 0 until numStr.length-1) {
        tmpNumList[i] = numStr[i]
        val tmpNum = (tmpNumList.joinToString("").toInt() - 1).toString()
        answer = maxOf(answer, calc(tmpNum))
    }

    bw.write("$answer")
    bw.close()
}

fun calc(numStr: String): Int {
    var tmpAns = 1
    for(i in 0 until numStr.length) {
        tmpAns *= numStr[i].toInt()
    }

    return tmpAns
}
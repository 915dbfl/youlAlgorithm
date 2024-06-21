import kotlin.math.max

val br = System.`in`.bufferedReader()
fun main() = with(System.out.bufferedWriter()) {
    val seq1 = br.readLine()
    val seq2 = br.readLine()
    val seq3 = br.readLine()

    val arr = Array(seq1.length+1) {Array(seq2.length+1) {IntArray(seq3.length+1)}}

    for (i in 1 until seq1.length+1) {
        for (j in 1 until seq2.length+1) {
            for(k in 1 until seq3.length+1) {
                arr[i][j][k] = if (seq1[i-1] == seq2[j-1] && seq2[j-1] == seq3[k-1]) {
                    arr[i-1][j-1][k-1] + 1
                } else {
                    maxOf(arr[i-1][j][k], arr[i][j-1][k], arr[i][j][k-1])
                }
            }
        }
    }

    
    write("${arr.last().last().last()}")
    close()
}
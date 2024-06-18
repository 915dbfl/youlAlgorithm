import java.io.*
import java.util.*

fun printPattern(i: Int, j: Int, size: Int, ans: Array<CharArray>) {
    if (size == 3) {
        ans[i][j] = '*'
        ans[i+1][j-1] = '*'
        ans[i+1][j+1] = '*'
        for (k in -2 until 3) {
            ans[i+2][j-k] = '*'
        }
    } else {
        val newSize = size.div(2)
        printPattern(i, j, newSize, ans)
        printPattern(i + newSize, j - newSize, newSize, ans)
        printPattern(i + newSize, j + newSize, newSize, ans)
    }
}

fun main() = with(System.`in`.bufferedReader()) {
    val n = readLine().toInt()
    val ans = Array(n){CharArray(2*n-1){' '}}
    printPattern(0, n-1, n, ans)

    print(ans.joinToString("\n"){it.joinToString("")})
    
}
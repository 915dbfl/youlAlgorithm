// 브루트포스 알고리즘
import java.util.*
import java.io.*
import kotlin.math.max

var answer = 0
val cutDx = listOf(0, -1, 0, 1)
val cutDy = listOf(1, 0, -1, 0)
lateinit var numArr: Array<ArrayList<Int>>
fun main() = with(System.`in`.bufferedReader()) {
    val (n, m) = readLine().split(" ").map {it.toInt()}

    // 누적합 활용
    numArr = Array(n){ArrayList()}
    for(i in 0 until n) {
        val row = readLine()
        for(ch in row) {
            val num = Character.getNumericValue(ch)
            numArr[i].add(num)
        }
    }

    cutPaper(0, n-1, 0, m-1, 0)
    print(answer)
}

fun cutPaper(startX: Int, endX: Int, startY: Int, endY: Int, sum: Int) {
    if (startX > endX || startY > endY) {
        answer = max(answer, sum)
        return
    }
    if(startX == endX && startY == endY) {
        answer = max(answer, sum + numArr[startX][startY])
        return
    }
    val h = endX - startX + 1
    val w = endY - startY + 1
    val time = listOf(w, h, w, h)

    for (i in 0 until 4) {
        var tmp = ""
        for (j in 0 until time[i]) {
            when(i) {
                0 -> tmp += numArr[startX][startY + j]
                1 -> tmp += numArr[startX + j][endY]
                2 -> tmp += numArr[endX][startY + j]
                3 -> tmp += numArr[startX + j][startY]
            }
        }
        when(i) {
            0 -> cutPaper(startX+1, endX, startY, endY, sum + tmp.toInt()) 
            1 -> cutPaper(startX, endX, startY, endY-1, sum + tmp.toInt())
            2 -> cutPaper(startX, endX-1, startY, endY, sum + tmp.toInt())
            3 -> cutPaper(startX, endX, startY+1, endY, sum + tmp.toInt())
        }
    }

}
// 비트 마스킹 풀이
import kotlin.math.max
val br = System.`in`.bufferedReader()

lateinit var graph: Array<IntArray>

fun main() = with(System.out.bufferedWriter()){

    //input
    val (n,m) =br.readLine().split(' ').map{it.toInt()}
    graph= Array(n){
        val line = br.readLine()
        IntArray(m){Character.getNumericValue(line[it])}
    }

    var answer=0
    for(state in 0 until (1 shl n*m)){
        var sum=0
        //가로
        for(r in 0 until n){
            var cur=0
            for(c in 0 until m){
                if(state and (1 shl r*m+c) ==0){
                    cur = cur*10 + graph[r][c]
                }
                else{
                    sum+=cur
                    cur=0
                }
            }
            sum+=cur
        }
        //세로
        for(c in 0 until m){
            var cur=0
            for(r in 0 until n){
                if(state and (1 shl r*m+c) !=0){
                    cur = cur*10 + graph[r][c]
                }
                else{
                    sum+=cur
                    cur=0
                }
            }
            sum+=cur
        }
        answer = max(answer, sum)
    }

    write("$answer")

    close()
}
// 28분
import java.io.*
import java.util.*
import kotlin.math.min

// 재귀
fun occupy(duck: Int, ground: Int, target: Int) {
    // 경로에 점유된 땅이 있을 경우
    if (occupied[ground]) {
        ducks[duck] = min(ground, ducks[duck])
    }
    // 루트에 도달했을 때
    if (ground == 1 && ducks[duck] == INF) {
        ducks[duck] = 0
        occupied[target] = true
        return 
    }
    else if(ground > 1){
        // 오른쪽 자식일 경우
        if(ground % 2 == 1) occupy(duck, (ground-1).div(2), target)
        // 왼쪽 자식일 경우
        else occupy(duck, ground.div(2), target)
    }
}

lateinit var occupied: BooleanArray
lateinit var ducks: IntArray
const val INF = Int.MAX_VALUE
val br = System.`in`.bufferedReader()
fun main() = with(System.out.bufferedWriter()) {
    val (n, q) = br.readLine().split(" ").map {it.toInt()}
    val wanted = IntArray(q) {
        br.readLine().toInt()
    }
    
    occupied = BooleanArray(n+1)
    ducks = IntArray(q){INF}
    for (i in 0 until q) {
        occupy(i, wanted[i], wanted[i])
        write("${ducks[i]}\n")
    }
    close()
}

// 간단한 풀이
val br = System.`in`.bufferedReader()
fun getIntList() = br.readLine().split(" ").map {it.toInt()}
fun getInt() = br.readLine().toInt()

fun main() = with(System.out.bufferedWriter()) {
    val (n, q) = getIntList()
    val set = mutableSetOf<Int>()

    repeat(q) {
        val origin = getInt()
        var num = origin
        var answer = 0
        while (num > 1) {
            if (set.contains(num)) answer = num
            num = num shr 1 // 나누기 2를 비트 연산으로 진행
        }
        write("$answer\n")
        if(answer == 0) set.add(origin)
    }
    close()
}
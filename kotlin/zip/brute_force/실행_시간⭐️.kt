// 오답
import java.util.StringTokenizer
import kotlin.collections.ArrayDeque
import kotlin.math.pow

val bw = System.out.bufferedWriter()

lateinit var order: Array<ArrayList<Int>>
lateinit var duration: IntArray

var n = 0
var m = 0
var k = 0
var endNum = 0

fun main() = with(System.`in`.bufferedReader()) {
    val st = StringTokenizer(readLine())
    n = st.nextToken().toInt()
    m = st.nextToken().toInt()
    k = st.nextToken().toInt()
    
    duration = readLine().split(" ").map {it.toInt()}.toIntArray()
    order = Array(n+1){ArrayList<Int>()}

    repeat(m) {
        val (s, e) = readLine().split(" ").map {it.toInt()}
        order[s].add(e)
    }

    endNum = findEnd()
    bw.write("${calcMinDuration()}")
    bw.close()
}

fun findEnd(): Int {
    var end = 0
    for (i in 2 until n+1) {
        if (order[i].size == 0) {
            end = i
            break
        }
    }

    return end
}

fun calcMinDuration(): Int {
    val combis = combination()
    // k=0일 경우 처리
    var minDuration = caclDuration(arrayListOf())

    for (combi in combis) {
        val tmpDur = caclDuration(combi)
        minDuration = minOf(minDuration, tmpDur)
    }

    return minDuration

}

fun caclDuration(combi: ArrayList<Int>): Int {
    val dq = ArrayDeque<Int>()
    val dis = IntArray(n+1)
    dq.add(1)
    dis[1] = duration[0]

    while (dq.isNotEmpty()) {
        val cur = dq.removeFirst()

        for (nxt in order[cur]) {
            if (!combi.contains(nxt)) {
                dis[nxt] = maxOf(dis[nxt], dis[cur] + duration[nxt-1])
            } else {
                dis[nxt] = maxOf(dis[nxt], dis[cur])
            }
            dq.add(nxt)
        }
    }

    return dis[endNum]
}

// 시작과 끝을 뺀 combination 구하기
fun combination(): ArrayList<ArrayList<Int>> {
    val nums = (2..n).filter {it != endNum}
    val combis = ArrayList<ArrayList<Int>>()
    for (i in 0 until (nums.size-k+1)) {
        val tmpList = ArrayList<Int>()
        repeat(k) {
            tmpList.add(nums[i+it])
        }
        combis.add(tmpList)
    }
    // println(combis.joinToString("\n") {it.joinToString()})
    return combis
}
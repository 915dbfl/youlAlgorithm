import java.util.PriorityQueue

fun main() = with(System.`in`.bufferedReader()) {
    val n = readLine().toInt()
    val pq = PriorityQueue<Int>()

    repeat(n) {
        val bundleCnt = readLine().toInt()
        pq.add(bundleCnt)
    }

    var total = 0
    while(pq.isNotEmpty()) {
        if (pq.size == 1) {
            break
        }
        val minBundle = pq.remove() + pq.remove()
        total += minBundle
        pq.add(minBundle)
    }
    print(total)
    
}
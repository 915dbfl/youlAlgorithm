// 96%에서 오답
import java.io.*
import java.util.*

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    var (n, k) = br.readLine().split(" ").map {it.toInt()}
    val level: ArrayList<Int> = ArrayList()

    for(i in 0 until n) {
        val l = br.readLine().toInt()
        level.add(l)
    }

    level.sort()

    for (i in 0 until n-1) {
        if (level[i+1] == level[i]) continue
        if (k >= (i+1) * (level[i+1] - level[i])) {
            k -= (i+1) * (level[i+1] - level[i])
        } else {
            if ((i+1) <= k) {
                print(level[i] + (k/(i+1)).toInt())
            } else {
                print(level[i])
            }
            k = 0
            break
        }
    } 

    if (k > 0) {
        if(n <= k) {
            print(level[n-1] + (k/n).toInt())
        } else {
            print(level[n-1])
        }
    }
}

// 이분탐색
// mid값 중 최대
fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    var (n, k) = br.readLine().split(" ").map {it.toInt()}
    val level: ArrayList<Int> = ArrayList()

    for(i in 0 until n) {
        val l = br.readLine().toInt()
        level.add(l)
    }

    level.sort()
    var s = level[0]
    var e = level[n-1] + k

    while (s <= e) {
        var mid = (s+e).div(2)
        var tmpK = 0

        var flag = true
        for(i in 0 until n) {
            var l = level[i]
            if (l < mid) {
                tmpK += mid - l
                if (tmpK > k) {
                    e = mid - 1
                    flag = false
                    break
                }
            }
        }
        if (flag) s = mid + 1
    }

    print(s-1)
}

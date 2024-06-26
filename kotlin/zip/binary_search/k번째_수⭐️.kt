// 이분 탐색

val br = System.`in`.bufferedReader()
var n = 0
var k = 0
var answer = 0

fun binarySearch(time: Int, left: Int, right: Int) {
    if (left >= right) {
        answer = left
        return
    }
    val mid = (left + right) / 2

    // A[i][j]의 값은 i*j임
    // i번째 행에 mid보다 작은 값은 mid/i만큼만 존재함
    var midCnt = 0
    for (i in 1 .. minOf(mid, n)) {
        midCnt += minOf(n, (mid/i))
    }

    // k: mid보다 작거나 같은 수가 적어도 k개는 존재해야 한다.
    // k와 midCnt를 비교해 left, right값을 조정한다.
    // 수를 높어야 함
    if (k >= midCnt) {
        binarySearch(time + 1, mid+1, right)
    // 수를 낮춰야 함
    } else {
        binarySearch(time + 1, left, mid-1)
    }
}

fun main() = with(System.out.bufferedWriter()) {
    n = br.readLine().toInt()
    // k의 의미: B[k]보다 같거나 작은 수의 개수가 총 k개 존재한다.
    k = br.readLine().toInt() 
    // B[k]값을 이분탐색으로 찾기
    // 이때 k는 무조건 찾고자 하는 수보다 크기 때문에 n*n대신 k를 넣어도 된다.
    binarySearch(0, 1, n*n)

    write("$answer")
    close()
}

// 가독성 좋은 코드✨
val br = System.`in`.bufferedReader()
val bw = System.out.bufferedWriter()
var n = 0L
var k = 0L

fun run() {
    input()
    bw.write("${solve()}")
    bw.close()
}

fun input() {
    n = br.readLine().toLong()
    k = br.readLine().toLong()
}

fun solve(): Long {
    var left = 1L
    var right = k
    while(left <= right) {
        val mid = (left+right)/2
        if (checkIndex(mid) >= k) {
            right = mid - 1
        } else {
            left = mid + 1
        }
    }

    return left
}

fun checkIndex(number: Long): Long {
    var sum = 0L
    for (i in 1 .. minOf(number, n)) {
        sum += minOf(n, (number/i))
    }
    return sum
}

fun main() {
    run()
}
/*
- 합 정렬 + 투 포인터
- 두 포인터가 가르키는 위치의 합이 0이 될 경우
    - ab 배열 포인터 이동, cd 배열 포인터 이동
- ab 배열 + cd 배열 > 0
    - ab 포인터 이동
- ab 배열 + cd 배열 < 0
    - cd 포인터 이동
 */

import java.util.StringTokenizer

fun main() = with(System.`in`.bufferedReader()) {
    val n = readLine().toInt()
    
    val A = IntArray(n)
    val B = IntArray(n)
    val C = IntArray(n)
    val D = IntArray(n)

    var st: StringTokenizer
    for (i in 0 until n) {
        st = StringTokenizer(readLine())
        A[i] = st.nextToken().toInt()
        B[i] = st.nextToken().toInt()
        C[i] = st.nextToken().toInt()
        D[i] = st.nextToken().toInt()
    }

    val ab = IntArray(n*n)
    val cd = IntArray(n*n)

    var index = 0
    for (i in 0 until n) {
        for (j in 0 until n) {
            ab[index] = A[i] + B[j]
            cd[index] = C[i] + D[j]
            index++
        }
    }

    ab.sort()
    cd.sort()

    var p1 = 0
    var p2 = ab.size - 1
    var answer = 0L

    while (p1 < ab.size && p2 >= 0) {
        if (ab[p1] + cd[p2] > 0) p2--
        else if (ab[p1] + cd[p2] < 0) p1++
        else {
            var countAB = 1L
            var countCD = 1L

            while (p1 < (ab.size - 1) && ab[p1] == ab[p1+1]) {
                countAB++
                p1++
            }
            while (p2 > 0 && cd[p2] == cd[p2 - 1]) {
                countCD++
                p2--
            }

            answer += countAB * countCD
            p1++
            p2--
        }
    }

    println(answer)
}
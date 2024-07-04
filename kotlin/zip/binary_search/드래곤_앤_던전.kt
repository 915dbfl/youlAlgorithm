// 1시간
// int 범위는 21억, 범위 잘 확인해서 알맞은 자료형 사용하기

import kotlin.math.*
import java.util.StringTokenizer

val br = System.`in`.bufferedReader()
val bw = System.out.bufferedWriter()

fun main() {
    val st = StringTokenizer(br.readLine())
    val n = st.nextToken().toInt()
    var atk = st.nextToken().toLong()
    val maxHps = ArrayList<Long>()

    var maxHp = 0L
    // 1, 몬스터 공격력, 몬스터 생명력
    // 2, 공격력 증가, 생명력 회복
    repeat(n) {
        val (t, a, h) = br.readLine().split(" ").map {it.toInt()}
        // 몬스터일 경우
        if (t == 1) {
            val time = ceil(h.toDouble() / atk).toLong()
            maxHp -= (time - 1) * a
        // 포션일 경우
        } else {
            // 해당 단계까지 와야하므로 maxHp 기록
            // 공격력 향상
            maxHps.add(-maxHp)
            atk += a
            // 감소한 생명력이 더 클 경우
            if (-maxHp > h) {
                maxHp += h
            } else {
                maxHp = 0L
            }
        }
    }

    maxHps.add(-maxHp)

    println(maxHps.max()+1)

}

// 이분탐색 풀이
import kotlin.math.ceil

lateinit var rooms: Array<LongArray>
fun main() = with(System.`in`.bufferedReader()) {
    val (n, atk) = readLine().split(" ").map {it.toLong()}
    rooms = Array(n.toInt()) {readLine().split(" ").map {it.toLong()}.toLongArray()}

    println(binarySearch(atk))
}

fun binarySearch(atk: Long): Long {
    var left = 1L
    var right = Long.MAX_VALUE

    while(left <= right) {
        val mid = (left + right) / 2

        // 해당 hp(mid)로 용 쓰러뜨리기 가능
        if (check(atk, mid)) {
            right = mid - 1
        // 해당 hp(mid)로 용 쓰러뜨리기 불가능
        } else {
            left = mid + 1
        }
    }
    
    return left
}

fun check(atk: Long, hp: Long): Boolean {
    var checkAtk = atk
    var checkHp = hp
    for ((t, a, h) in rooms) {
        when(t) {
            1L -> {
                checkHp -= (ceil(h.toDouble() / checkAtk).toLong() - 1) * a
                if (checkHp <= 0L) return false
            }
            2L -> {
                checkHp = if (checkHp + h > hp) hp else checkHp + h
                checkAtk += a
            }
        }
    }

    return checkHp > 0L
}
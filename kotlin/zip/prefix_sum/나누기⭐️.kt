/*
풀이 과정
1. 누적합 구하기
2. 전체 누적합 / 4 != 0
    - 동일한 누적합으로 4등분 불가능
3. dp 재귀 호출
 */

private lateinit var prefix: LongArray
private lateinit var dp: Array<LongArray>

private fun calCase(
    index: Int,
    cnt: Int, 
    k: Long,
    n: Int
): Long {
    // 4등분이 완료되었을 경우
    if (cnt == 3) {
        return if (index < n) 1 else 0
    }

    // 유효한 인덱스가 아닐 때
    if (index >= n) {
        return 0
    }

    // dp 계산하기
    if (dp[index][cnt] != -1L) {
        return dp[index][cnt]
    }

    // dp 계산하기
    dp[index][cnt] = 0
    if (prefix[index] == (cnt + 1) * k) {
        dp[index][cnt] += calCase(index+1, cnt+1, k, n)
    }
    dp[index][cnt] += calCase(index+1, cnt, k, n)

    return dp[index][cnt]
}

fun main() = with(System.`in`.bufferedReader()) {
    val n = readLine().toInt()
    val nums = readLine().split(" ").map {it.toInt()}.toIntArray()

    prefix = LongArray(n)
    prefix[0] = nums[0].toLong()
    dp = Array(n) {LongArray(4) {-1L}}

    // 누적합 계산
    for (i in 1 until n) {
        prefix[i] += prefix[i-1] + nums[i]
    }

    // 4등분 할 수 있는지 확인
    if (prefix[n-1] % 4 != 0L) {
        println(0)
    } else {
        val k = prefix[n-1] / 4
        println(calCase(0, 0, k, n))
    }
}

/*
풀이과정 - 누적합 (60점)
1. 누적합으로 합 저장
2. 세 개의 index 구하기
    - 전체에서 양쪽 합이 같은 index 하나 구하기(O(십만))
    - 각 양쪽에서 합이 같은 Index 하나 구하기(O(십만))
3. 전체 방법수...?
    - 우선 양쪽 합이 같은 index 구하는 모든 경우의 수 계산
    - 내부 함수 호출을 통해 그 속에서 각 양쪽 합이 같은 index 구하는 방법 호출
 */

 fun main() = with(System.`in`.bufferedReader()) {
    val n = readLine().toInt()
    val nums = readLine().split(" ").map { it.toInt()}.toIntArray()
    
    val prefix = LongArray(n) {0L}
    prefix[0] = nums[0]

    for (i in 1 until n) {
        prefix[i] += prefix[i-1] + nums[i]
    }

    fun findMiddle(start: Int, end: Int, base: Long): Long {
        var cnt = 0L
        // 합이 동일한 두 덩이로 나눌 index 구하기
        for (i in start until end) {
            val left = prefix[i] - base
            val right = prefix[end] - prefix[i]
            if (left == right) {
                cnt += 1
            }
        }
        return cnt
    }

    var answer = 0L
    for (i in 0 until n) {
        val left = prefix[i]
        val right = prefix[n-1] - prefix[i]
        if (left == right) {
            val leftCase = findMiddle(0, i, 0)
            val rightCase = findMiddle(i+1, n-1, left)
            answer += leftCase * rightCase
        }
    }

    print(answer)
}
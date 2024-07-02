// napsack 알고리즘
// 오답
val br = System.`in`.bufferedReader()
val bw = System.out.bufferedWriter()
var maxCpu = 0
var maxMemory = 0
var answer = 501

fun main() {
    val (n, m, k) = br.readLine().split(" ").map {it.toInt()}
    val tabsInfo = Array(n) {IntArray(3)}
    
    repeat(n) {
        val (c, m, p) = br.readLine().split(" ").map {it.toInt()}
        maxCpu += c
        maxMemory += m
        tabsInfo[it] = intArrayOf(c, m, p)
    }
    // println(tabsInfo.joinToString("\n"){it.joinToString()})

    if (maxCpu < m || maxMemory < k) {
        bw.write("-1")
        bw.close()
    } else {
        // m의 최댓값이 k의 최댓값보다 작기 때문에 m을 가지고 dp 구성
        // dp[i][j][k] : [ 메모리 할당량 합, 최소 우선순위 합 ]
        val dp = Array(n) {Array(n*m+1) {IntArray(2)}}

        for (i in tabsInfo[0][0] until m+1) {
            dp[0][i] = intArrayOf(tabsInfo[0][1], tabsInfo[0][2])
        }

        for (i in 1 until n) {
            for (j in tabsInfo[i][0] until n*m+1) {
                // 두 목표 메모리 할당량 비교
                val p1 = dp[i-1][j][0]
                val p2 = dp[i-1][j-tabsInfo[i][0]][0] + tabsInfo[i][1]
                val priority1 = dp[i-1][j][1]
                val priority2 = dp[i-1][j-tabsInfo[i][0]][1] + tabsInfo[i][2]
                
                // 두 경우 모두 목표 메모리 할당량을 넘은 경우
                if (p1 >= k && p2 >= k) {
                    // 중요도 합이 작은 것을 선택
                    if (priority1 <= priority2) {
                        dp[i][j] = intArrayOf(p1, priority1)
                    } else {
                        dp[i][j] = intArrayOf(p2, priority2)
                    }
                } else {
                    if (p1 >= p2) {
                        dp[i][j] = intArrayOf(p1, priority1)
                    } else {
                        dp[i][j] = intArrayOf(p2, priority2)
                    }
               
                }

                if (j >= m && dp[i][j][0] >= k) {
                    answer = minOf(answer, dp[i][j][1])
                }
                
            }
        }

        // println(dp.joinToString("\n"){it.joinToString() {it.joinToString(",")}})

        bw.write("${if(answer == 501) -1 else answer}")
        bw.close()
    }
}

// 정답 풀이
// dp[i][j]: 우선순위합 i && cpu합이 j일 때 최대 메모리 확보량 저장

val br = System.`in`.bufferedReader()
val bw = System.out.bufferedWriter()
const val N_MAX = 100
const val M_MAX = 1000 // cpu합 최대
const val P_MAX = 500 // 우선순위합 최대

fun main() {
    val (N, M, K) = br.readLine().split(" ").map {it.toInt()}
    // cpu, memory, priority
    val tabsInfo = Array(N) {
        br.readLine().split(" ").map {it.toInt()}
    }

    // dp[i][j]: 우선순위합 i && cpu합이 j일 때 최대 메모리 확보량
    // 초기화를 무한대 음수로 해야 도달할 수 없는 경우를 명확히 표시할 수 있다.
    val dp = Array(P_MAX+1) {IntArray(M_MAX+1) {-Int.MAX_VALUE}}
    dp[0][0] = 0

    // n개의 탭에 대해서
    for (i in 0 until N) {
        // 우선순위 합이 j일 경우
        // priority를 큰수부터 확인하는 이유
        // priority에 memory의 최대값이 반영되어야 조건을 만족하는 priority의 최솟값을 구할 수 있기 때문
        for (j in P_MAX downTo 0) {
            // cpu 합이 k일 경우
            for (k in 0 until M_MAX+1) {
                // 우선순위의 합이 최대 우선순위 합을 넘은 경우 예외처리
                if (j + tabsInfo[i][2] > P_MAX) continue

                // cpu 사용량 합이 목표 사용량보다 작을 경우
                if (k + tabsInfo[i][0] <= M_MAX) {
                    dp[j + tabsInfo[i][2]][k + tabsInfo[i][0]] = maxOf(dp[j + tabsInfo[i][2]][k + tabsInfo[i][0]], dp[j][k] + tabsInfo[i][1])
                // cpu 사용량 합이 목표 사용량보다 클 경우
                } else {
                    dp[j + tabsInfo[i][2]][M_MAX] = maxOf( dp[j + tabsInfo[i][2]][M_MAX], dp[j][k] + tabsInfo[i][1])
                }
            }
        }
    }

    var answer = P_MAX+1
    for (i in 0 until P_MAX+1) {
        for (j in M until M_MAX+1) {
            if (dp[i][j] >= K) {
                answer = minOf(answer, i)
            }
        }
    }

    bw.write("${if (answer == P_MAX+1) -1 else answer}")
    bw.close()
    
}
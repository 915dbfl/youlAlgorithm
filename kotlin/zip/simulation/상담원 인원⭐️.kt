// 시간 초과 - 2/8 재풀이 필요
import kotlin.math.*
import java.util.PriorityQueue

class Solution {
    private val applications = mutableMapOf<Int, ArrayList<Application>>()
    private lateinit var waitingTimes: Array<IntArray>
    private lateinit var mentorCntList: IntArray
    private var answer = Int.MAX_VALUE
    
    fun solution(k: Int, n: Int, reqs: Array<IntArray>): Int {
        for ((a, b, c) in reqs) {
            if (applications.get(c) == null) {
                applications[c] = arrayListOf(Application(a, b, c))
            } else {
                applications[c]!!.add(Application(a, b, c))    
            }
        }
        
        val maxMentoCnt = n - k + 1
        waitingTimes = Array(k+1) { IntArray(maxMentoCnt+1){Int.MAX_VALUE} }
        calAllCaseWaitingTime(k, maxMentoCnt)
        
        mentorCntList = IntArray(k+1){1}
        calMinWaintingTime(k, n)
        
        return answer
    }
    
    private fun calMinWaintingTime(
        k: Int,
        n: Int,
    ) {
        if (mentorCntList.sum() - 1 == n) {
            answer = min(answer, calTotalWaitingTime(k))
            return
        }
        
        for (type in 1 until k+1) {
            // 불필요한 재귀 가지치기
            val appList = applications.getOrDefault(type, arrayListOf())
            if (mentorCntList[type] > 1 && appList.size < mentorCntList[type] + 1) continue
            mentorCntList[type] += 1
            calMinWaintingTime(k, n)
            mentorCntList[type] -= 1
        }
    }
    
    private fun calTotalWaitingTime(k: Int): Int {
        var total = 0
        var mentorCnt: Int
        var wt: Int
        for (type in 1 until k+1) {
            mentorCnt = mentorCntList[type]
            wt = waitingTimes[type][mentorCnt]
            if (wt == Int.MAX_VALUE) {
                return Int.MAX_VALUE
            }
            total += wt
        }
        return total
    }
    
    private fun calAllCaseWaitingTime(
        k: Int,
        maxMentoCnt: Int
    ) {
        // 각 유형별로
        for (i in 1 until k+1) {
            val appList = applications.getOrDefault(i, arrayListOf())
            // 멘토수에 따라
            // 불필요한 계산 가지치기
            for (j in 1 until maxMentoCnt+1) {
                if (j > 1 && appList.size < j) break
                calWaitingTimeByMentoCnt(i, j)
            }
        }
    }
    
    private fun calWaitingTimeByMentoCnt(
        type: Int,
        mCnt: Int,
    ) {
        val pq = PriorityQueue<Int>(compareBy {it})
        // 멘토 초기화
        for (i in 0 until mCnt) {
            pq.offer(0)
        }
        
        var wt = 0
        var appIdx = 0
        val appLists = applications[type] ?: arrayListOf()
        while(appIdx < appLists.size) {
            // 다음 멘토 꺼내기
            val mBusy = pq.poll()
            
            // 대기 시, 계산
            if (appLists[appIdx].start < mBusy) {
                wt += mBusy - appLists[appIdx].start
            }
            
            // 멘토 busy time 업데이트
            val realStartTime = max(appLists[appIdx].start, mBusy)
            pq.offer(realStartTime + appLists[appIdx].duration)
            appIdx += 1
        }
        waitingTimes[type][mCnt] = wt
    }
}

data class Application(
    val start: Int, 
    val duration: Int, 
    val type: Int
)
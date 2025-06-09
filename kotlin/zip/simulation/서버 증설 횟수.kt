/*
풀이
- 시간만큼 반복문을 진행한다.
- 현재 서버 수를 기록하고 있는다.
- 만약 n * m <= 현재 이용자 수 < (n+1) * m라면 n개만큼 서버를 증설해야 한다.
- 서버는 k시간 동안만 운영이 되기 때문에 서버를 증설할 때 k시간 후에 -1을 기록한다.(누적합 활용)
*/

class Solution {
    fun solution(players: IntArray, m: Int, k: Int): Int {
        // 시간대별 증설 서버수 기록 배열
        val serverCnt = IntArray(24 + k)
        var curServerCnt: Int
        var needServer: Int
        var answer: Int = 0
        
        // 시간대 만큼 반복
        repeat(24) { time ->
        
            // 증설 서버 계산
            needServer = players[time] / m
            curServerCnt = serverCnt[time]
            if(needServer > curServerCnt) {
                val addServerCnt = needServer - curServerCnt
                answer += addServerCnt
                serverCnt[time] += addServerCnt
                serverCnt[time + k] -= addServerCnt
            }
            serverCnt[time + 1] += serverCnt[time]
        }
        
        return answer
    }
}

// 큐활용
class Solution {
    fun solution(players: IntArray, m: Int, k: Int): Int {
        var answer: Int = 0
        var pq = ArrayDeque<Int>()
        var serversToAdd: Int
        
        players.forEachIndexed { i, p ->
            while(!pq.isEmpty() && (i - pq.first() >= k)) pq.removeFirst()
            
            val cur = pq.size
            if(p / m > cur) {
                serversToAdd = p/m - cur
                repeat(serversToAdd) {
                    pq.add(i)
                    answer += 1
                }
            }
        }
        
        return answer
    }
}
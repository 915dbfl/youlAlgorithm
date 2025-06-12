/*
해설
- 1<= level <= 100,000
- 총 300,000개의 문제를 품
- level에서 이분 탐색 -> log(100,000) * 300,000을 진행
*/

import java.lang.Math;

class Solution {
    private static final int MAX_LEVEL = 300000;
    private static final int MIN_LEVEL = 1;
    
    private int problemNum;
    
    public int solution(int[] diffs, int[] times, long limit) {
        problemNum = diffs.length;
        
        int start = MIN_LEVEL;
        int end = MAX_LEVEL;
        int minLevel = 100001;
        
        while(start <= end) {
            int mid = (start + end)/ 2;
            
            if(canSolve(mid, diffs, times, limit)) {
                minLevel = Math.min(minLevel, mid);
                end = mid - 1;
            } else {
                start = mid + 1;
            }
        }
        
        return minLevel;
    }
    
    private boolean canSolve(
        int level,
        int[] diffs,
        int[] times,
        long limit
    ) {
        long curTime = 0;
        
        for(int i = 0; i < problemNum; i++) {
            if(diffs[i] <= level) {
                curTime += times[i];
            } else {
                int time_prev = (i == 0) ? 0 : times[i-1];
                int retry = diffs[i] - level;
                // long으로 형변환해서 오버플로우 방지
                curTime += (long) retry * (times[i] + time_prev);
                curTime += times[i];
            }
            
            if(curTime > limit) return false;
        }
        
        return limit >= curTime;
    }
}
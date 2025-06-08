package java_algorithm.zip.dp;
import java.util.*;

class Solution {
    public int solution(int[][] info, int n, int m) {
        Map<Integer, Integer> aDict = new HashMap<>();
        aDict.put(0, 0); // 초기 상태: A 흔적 0일 때 B 흔적도 0

        // 각 물건 (aCost, bCost)에 대해 반복
        for (int[] item : info) {
            int aCost = item[0];
            int bCost = item[1];

            Map<Integer, Integer> newDict = new HashMap<>();

            // aDict에 저장된 모든 이전 상태 (aa: A 흔적, ab: B 흔적)에 대해 반복
            for (Map.Entry<Integer, Integer> entry : aDict.entrySet()) {
                int aa = entry.getKey();   // 이전 A의 누적 흔적
                int ab = entry.getValue(); // 이전 B의 누적 흔적

                // 1. 현재 물건을 A가 훔칠 경우
                int nextAa = aa + aCost; // A의 새로운 누적 흔적
                int nextAb = ab;         // B의 누적 흔적은 그대로

                // 새로운 상태가 n, m 제한을 넘지 않는지 확인
                if (nextAa < n && nextAb < m) {
                    // newDict에 nextAa 키가 없거나, 현재 nextAb 값이 기존 값보다 작을 때 업데이트
                    if (!newDict.containsKey(nextAa) || newDict.get(nextAa) > nextAb) {
                        newDict.put(nextAa, nextAb);
                    }
                }

                // 2. 현재 물건을 B가 훔칠 경우
                nextAa = aa;             // A의 누적 흔적은 그대로
                nextAb = ab + bCost;     // B의 새로운 누적 흔적

                // 새로운 상태가 n, m 제한을 넘지 않는지 확인
                if (nextAa < n && nextAb < m) {
                    // newDict에 nextAa 키가 없거나, 현재 nextAb 값이 기존 값보다 작을 때 업데이트
                    if (!newDict.containsKey(nextAa) || newDict.get(nextAa) > nextAb) {
                        newDict.put(nextAa, nextAb);
                    }
                }
            }
            
            // 모든 유효한 조합이 n, m 제한을 초과하여 newDict가 비어버린 경우
            if (newDict.isEmpty()) {
                return -1;
            }
            
            // 현재 단계에서 계산된 새로운 상태들을 다음 반복을 위한 aDict로 설정
            aDict = newDict;
        }

        return aDict.keySet().stream().min(Integer::compare).orElse(-1);
    }
}
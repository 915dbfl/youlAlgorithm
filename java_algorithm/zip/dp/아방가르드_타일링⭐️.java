package java_algorithm.zip.dp;
import java.util.ArrayList;
import java.util.List;

public class 아방가르드_타일링 {
    private final int MOD = 1_000_000_007; 

    public int solution(int n) {
        List<Integer> dp = new ArrayList<>();
        dp.add(0); // dp[0]
        dp.add(1); // dp[1]
        dp.add(3); // dp[2]
        dp.add(10); // dp[3]
        dp.add(23); // dp[4]
        dp.add(62); // dp[5]
        dp.add(170); // dp[6]

        if (n < 7) {
            return dp.get(n);
        }

        for (int i = 7; i <= n; i++) {
           long x = (dp.get(dp.size() - 1).longValue() +
              2L * dp.get(dp.size() - 2).longValue() +
              6L * dp.get(dp.size() - 3).longValue() +
              dp.get(dp.size() - 4).longValue() -
              dp.get(dp.size() - 6).longValue());
            
            x %= MOD;
            // x가 음일 경우 처리
            if (x < 0) {
                x += MOD;
            }
            
            // 6 사이즈 유지
            dp.remove(0);
            dp.add((int)x);
        }

        return dp.get(dp.size() - 1);
    }
}

package java_algorithm.zip.prefix_sum;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Arrays;
import java.util.StringTokenizer;
import java.util.HashMap;

// 누적합⭐️ 
// dp[0]인 구간을 포함해야함!

public class 수열의_구간_평균 {
    final static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        long[] nums = Arrays.stream(br.readLine().split(" ")).mapToLong(Long::parseLong).toArray();
        long[] dp = new long[n+1];

        for(int i = 0; i < n; i++) {
            dp[i+1] = dp[i] + nums[i];
        }

        HashMap<Long, Integer> hm = new HashMap<>();
        for(int i = 0; i<= n; i++) {
            long diff = dp[i] - k * (i+1);
            if(hm.containsKey(diff)) {
                hm.replace(diff, hm.get(diff)+1);
            } else {
                hm.put(diff, 1);
            }
        }

        int ans = 0;
        for(long key: hm.keySet()) {
            int v = hm.get(key);
            ans += (v * (v-1)) / 2;
        }

        System.out.println(ans);
    }
    
}

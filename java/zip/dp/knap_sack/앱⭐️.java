package youlAlgorithm.java.zip.dp.knap_sack;
// m <= 10000000
// 메모리를 기준으로 index를 잡으면 메모리 초과
// cost를 기준으로 index 잡음

import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.Arrays;

public class 앱 {

    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String args[]) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int ans = Integer.MAX_VALUE;

        // dp[i][j]: i번째 앱을 포함했을 때 j비용으로 얻을 수 있는 최대 메모리
        int[][] dp = new int[n][100001];

        int[] memoryArr = Arrays.stream(br.readLine().split(" "))
        .mapToInt(Integer::parseInt).toArray();
        int[] costArr = Arrays.stream(br.readLine().split(" "))
        .mapToInt(Integer::parseInt).toArray();

        for(int i = 0; i < n; i++) {
            int cost = costArr[i];
            int memory = memoryArr[i];

            for(int j = 0; j <= 10000; j++) {
                if (i == 0) {
                    if (j >= cost) dp[i][j] = memory;
                }else {
                    if (j >= cost) dp[i][j] = Math.max(dp[i-1][j-cost] + memory, dp[i-1][j]);
                    else dp[i][j] = dp[i-1][j];
                }
                if (dp[i][j] >= m) ans = Math.min(ans, j);
            }
        }

        System.out.println(ans);
        br.close();
        
    }
    
}

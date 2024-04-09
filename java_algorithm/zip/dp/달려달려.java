import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.io.IOException;

public class 달려달려 {
    final static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static int[] dist;
    static int ans = 0;
    static int n, m;

    public static void main(String[] args) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        dist = new int[n];
        
        for(int i = 0; i < n; i++) {
            dist[i] = Integer.parseInt(br.readLine());
        }

        int[][] dp = new int[n][m+1];
        dp[0][0] = 0;
        dp[0][1] = dist[0];
        dp[1][0] = dist[0];

        for(int i = 1; i < n; i++) {
            for(int j = 0; j < m+1; j++) {
                // 지침지수가 0일 경우
                if (j > i+1) break;
                if(j == 0) {
                    dp[i][j] = Math.max(dp[i-1][j], dp[i][j]);
                } else {    
                    dp[i][j] = dp[i-1][j-1] + dist[i];
                    if (i+j < n) {
                        dp[i+j][0] = Math.max(dp[i+j][0], dp[i][j]);
                    }

                } 
            }
        }

        System.out.println(dp[dp.length-1][0]);
    }
}

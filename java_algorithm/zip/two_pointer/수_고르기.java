package youlAlgorithm.java.zip.two_pointer;

import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.Arrays;

public class 수_고르기 {
    final static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        Long[] arr = new Long[n];

        for(int i = 0; i < n; i++) {
            arr[i] = Long.parseLong(br.readLine());
        }

        // 오름차순으로 정렬
        Arrays.sort(arr);

        int p1 = 0;
        int p2 = 0;

        if(m == 0 || n == 1) {
            System.out.println(0);
            br.close();
        } else {
            Long ans = 2000000001L;
            // 투포인터 활용
            while(p2 < n) {
                // p2 - p1 >= m일 때
                if(arr[p2] - arr[p1] >= m) {
                    Long tmp = arr[p2] - arr[p1];
                    while (tmp >= m) {
                        p1 += 1;
                        tmp = arr[p2] - arr[p1];
                    } 

                    if (p1 > 0) {
                        Long tmpAns = arr[p2] - arr[p1-1];
                        ans = Math.min(ans, tmpAns);
                    }
                    
                } else {
                    p2 += 1;
                }
            }

            System.out.println(ans);
            br.close();
        }
    }
}
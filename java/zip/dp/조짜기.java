package youlAlgorithm.java.zip.dp;

import java.util.Scanner;
import java.util.Arrays;

public class 조짜기 {
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        sc.nextLine();
        String str[] = sc.nextLine().split(" ");
        int arr[] = new int[n];
        int dp[] = new int[n];

        for (int i = 0; i < str.length; i++) {
            arr[i] = Integer.parseInt(str[i]);
        }
        // System.out.println(Arrays.toString(arr));

        if (n > 2) {
            dp[1] = Math.abs(arr[0] - arr[1]);
        }

        for(int i = 2; i < n; i++) {
            int min = arr[i];
            int max = arr[i];

            for(int j = i; j >= 0; j--) {
                if(arr[j] > max) {
                    max = arr[j];
                } else if(arr[j] < min) {
                    min = arr[j];
                }

                int tmp = max - min;
                if(j-1 > 0) {
                    tmp += dp[j-1];
                }

                dp[i] = Math.max(dp[i], tmp);
            }
        }

        System.out.println(dp[n-1]);

    }

}
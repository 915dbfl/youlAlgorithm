package java_algorithm.zip.divide_conquer;
/*
 * 투에 모스 문자열 규칙 확인
 * 짝수 n -> n/2 문자와 동일
 * 홀수 n -> n/2 문자와 반대
*/

import java.io.*;
import java.util.StringTokenizer;

public class 투에_모스_문자열 {
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        long k = Long.parseLong(st.nextToken());
        System.out.println((divideConquer(k-1)) ? 1 : 0);
    }

    private static boolean divideConquer(long idx) {
        if(idx == 0) {
            return false;
        }
        if(idx % 2 == 1) {
            return !divideConquer(idx/2);
        } else {
            return divideConquer(idx/2);
        }
    }
}

/*
 * 투에 모스 문자열 점화식
 * n <= 1 -> return n;
 * n % 2 == 0 -> return 재귀(n/2)
 * n % 2 == 1 -> return 1 - 재귀(n/2)
 * 
public class Main {
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        long k = Long.parseLong(st.nextToken());
        System.out.println(divideConquer(k-1));
    }

    private static long divideConquer(long num) {
        if(num <= 1) return num;
        if(num % 2 == 1) {
            return 1 - divideConquer(num / 2);
        } else {
            return divideConquer(num / 2);
        }
    }
}
 */
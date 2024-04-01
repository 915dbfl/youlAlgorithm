package youlAlgorithm.java.zip.recursion;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;
import java.util.Arrays;

public class 종이의_개수 {
    final static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static int[][] papers;
    final static int[] answer = {0, 0, 0};

    private static Boolean checkPaper(int x, int y, int l) {
        int base = papers[x][y];
        for(int i = x; i < x+l; i++) {
            for(int j = y; j < y+l; j++) {
                if(base != papers[i][j]) {
                    return false;
                }
            }
        }

        answer[base+1] += 1;
        return true;
    }

    private static void cutPaper(int x, int y, int l) {
        if (!checkPaper(x, y, l)) {
            int tmpL = (int)l/3;
            System.out.println(String.format("%d %d %d", x, y, tmpL));
            for(int i = 0; i < 3; i++) {
                for(int j = 0; j < 3; j++) {
                    cutPaper(x+i*tmpL, y+j*tmpL, tmpL);
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st;

        papers = new int[n][n];

        for(int i = 0; i < n; i++) {
            papers[i] = Arrays.stream(br.readLine().split(" "))
            .mapToInt(Integer::parseInt).toArray();
            
        }
        
        cutPaper(0, 0, n);
        System.out.println(answer[0]);
        System.out.println(answer[1]);
        System.out.println(answer[2]);
    }
}

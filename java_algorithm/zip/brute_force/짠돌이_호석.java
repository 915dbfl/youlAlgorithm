package youlAlgorithm.java_algorithm.zip.brute_force;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.io.IOException;
import java.util.Arrays;
import java.util.StringTokenizer;

// 돌리는 퍼즐이 기준이 되는 퍼즐보다 오른쪽 위에 위치할 수 있다는 것을 명심 또 명심!!!

public class 짠돌이_호석 {
    final static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static int[][] puzzle1;
    static int[][] puzzle2;

    public static int[][] rotate(int[][] puzzle) {
        int n = puzzle.length;
        int m = puzzle[0].length;
        int[][] newPuzzle = new int[m][n];

        for(int i = 0; i < m; i++) {
            for(int j = 0; j < n; j++) {
                newPuzzle[i][j] = puzzle[n-1-j][i];
            }
        }

        return newPuzzle;
    }

    public static boolean matchPuzzle(int x, int y) {
        for(int i = 0; i < puzzle2.length; i++) {
            for(int j = 0; j < puzzle2[0].length; j++) {
                // 범위 안에 있다면
                if (i+x < puzzle1.length && j+y < puzzle1[0].length) {
                    // 겹치는지 확인
                    if(puzzle1[i+x][j+y] == 1 && puzzle2[i][j] == 1) {
                        return false;
                    }
                }
            }
        }

        return true;

    }

    public static void main(String[] args) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n1 = Integer.parseInt(st.nextToken());
        int m1 = Integer.parseInt(st.nextToken());

        puzzle1 = new int[n1][m1];
        for(int i = 0; i < n1; i++) {
            puzzle1[i] = Arrays.stream(br.readLine().split("")).mapToInt(Integer::parseInt).toArray();
        }

        st = new StringTokenizer(br.readLine());
        int n2 = Integer.parseInt(st.nextToken());
        int m2 = Integer.parseInt(st.nextToken());

        puzzle2 = new int[n2][m2];
        for(int i = 0; i < n2; i++) {
            puzzle2[i] = Arrays.stream(br.readLine().split("")).mapToInt(Integer::parseInt).toArray();
        }

        int ans = 10201;
        int tmpCol, tmpRow;
        // 90, 180, 270, 360 회전하며 match 진행
        for(int i = 0; i < 4; i++) {
            puzzle2 = rotate(puzzle2);
            tmpRow = Math.max(puzzle2.length, puzzle1.length);
            tmpCol = puzzle1[0].length + puzzle2[0].length;
            ans = Math.min(ans, tmpRow*tmpCol);

            tmpRow = puzzle1.length + puzzle2.length;
            tmpCol = Math.max(puzzle1[0].length, puzzle2[0].length);
            ans = Math.min(ans, tmpRow*tmpCol);

            for(int j = -puzzle2.length+1; j < n1; j++) {
                for(int k = -puzzle2[0].length+1; k < m1; k++) {
                    if(matchPuzzle(j, k)) {
                        if(j < 0) tmpRow = Math.abs(j) + puzzle1.length
                        else tmpRow = Math.max(j + puzzle2.length, puzzle1.length);
                        tmpCol = Math.max(k + puzzle2[0].length, puzzle1[0].length);

                        if (ans > tmpCol * tmpRow) {
                            ans = tmpCol * tmpRow;
                        }

                    }
                }
            }
        }

        System.out.println(ans);
        br.close();
    }
}

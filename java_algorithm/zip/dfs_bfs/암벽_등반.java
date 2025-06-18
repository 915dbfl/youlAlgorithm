package java_algorithm.zip.dfs_bfs;
// bfs
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.HashSet;
import java.util.Objects;
import java.util.Queue;
import java.util.Set;
import java.util.StringTokenizer;
import java.lang.Math;

public class 암벽_등반 {
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static StringTokenizer st;
    private static Set<Coordinate> wholeSet;

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int t = Integer.parseInt(st.nextToken());
        int width = 0;
        wholeSet = new HashSet<>();

        for(int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int y = Integer.parseInt(st.nextToken());
            int x = Integer.parseInt(st.nextToken());
            width = Math.max(width, y);
            wholeSet.add(new Coordinate(x, y));
        }

        // 출력
        System.out.println(bfs(t, width));
    }

    private static int bfs(int t, int width) {
        Queue<CoordinateWithMCnt> queue = new ArrayDeque<>();
        Coordinate start = new Coordinate(0, 0);
        boolean[][] visited = new boolean[t+1][width+1];
        queue.add(new CoordinateWithMCnt(start, 0));

        while(!queue.isEmpty()) {
            CoordinateWithMCnt cur = queue.poll();

            if (cur.cd.x == t) {
                return cur.mCnt;
            }

            if(visited[cur.cd.x][cur.cd.y]) continue;
            visited[cur.cd.x][cur.cd.y] = true;

            for(int i = -2; i <= 2; i++) {
                for(int j = -2; j <= 2; j++) {
                    int nx = cur.cd.x + i;
                    int ny = cur.cd.y + j;

                    // 범위 내인지 확인
                    if (0 <= nx && nx <= t && 0 <= ny && ny <= width) {
                        // 홈이 있고, 더 짧은 루트로 방문이 가능할 경우
                        if (visited[nx][ny]) continue;
                        Coordinate nxt = new Coordinate(nx, ny);
                        if (wholeSet.contains(nxt)) {
                            queue.add(new CoordinateWithMCnt(nxt, cur.mCnt + 1));
                        }
                    }
                }
            }
        }

        return -1;
    }

    private static class Coordinate {
        int x;
        int y;

        public Coordinate(int x, int y) {
            this.x = x;
            this.y = y;
        }

        @Override
        public int hashCode() {
            return Objects.hash(x, y);
        }

        @Override
        public boolean equals(Object obj) {
            if (this == obj) return true;
            if (obj == null || getClass() != obj.getClass()) return false;
            Coordinate that = (Coordinate) obj;
            return this.x == that.x && this.y == that.y;
        }
    }

    private static class CoordinateWithMCnt {
        Coordinate cd;
        int mCnt;

        public CoordinateWithMCnt(Coordinate cd, int mCnt) {
            this.cd = cd;
            this.mCnt = mCnt;
        }
    }
}

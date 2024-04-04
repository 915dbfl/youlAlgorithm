package java_algorithm.zip.bellman_ford;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.io.IOException;
import java.util.StringTokenizer;
import java.util.concurrent.atomic.LongAccumulator;
import java.util.ArrayList;
import java.util.Arrays;

// 벨만 포드 알고리즘 -> O(VE)
// 주의할 점
// int로 dist를 설정할 경우 음수 순환애서 underOverflow가 발생할 수 있다.
// underOverflow의 경우 최소값 갱신이 진행되지 않는다.

class Road{
    int a;
    int b;
    int c;

    Road(int a, int b, int c) {
        this.a = a;
        this.b = b;
        this.c = c;
    }
}

public class 타임머신 {
    final static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static ArrayList<Road> roads;
    static Long[] dist;
    static Long INF = Long.MAX_VALUE;

    public static boolean bellmanFord(int n, int m, int start) {
        dist = new Long[n];
        Arrays.fill(dist, INF);
        dist[start-1] = 0L;

        // 노드 전체 돌기
        for(int i = 0; i < n; i++) {
            // 매번 모든 간선 확인
            // 해당 for문을 다 돌았을 때 될 수 있는 최대 음수: -60000000
            for(int j = 0; j < m; j++) {
                Road curRoad = roads.get(j);

                if(dist[curRoad.a-1] != INF && dist[curRoad.b-1] > dist[curRoad.a-1] + curRoad.c) {
                    dist[curRoad.b-1] = dist[curRoad.a-1] + curRoad.c;

                    // 음의 순환인지 파악
                    if (i >= n-1) {
                        return false;
                    }
                }
            }
        }

        return true;
    }

    public static void main(String[] args) throws IOException {
        StringTokenizer st  = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        roads = new ArrayList<>();
        for(int i  = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());

            roads.add(new Road(a, b, c));
        }

        boolean result = bellmanFord(n, m, 1);
        if (result) {
            for(int i = 1; i < n; i++) {
                if(dist[i] == INF) {
                    System.out.println(-1);
                } else {
                    System.out.println(dist[i]);
                }
            }
        } else {
            System.out.print(-1);
        }

        br.close();
    }

}

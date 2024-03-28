package youlAlgorithm.java.algorithm_notes;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Floyd {
    static final int INF = Integer.MAX_VALUE;

    public static void floyd(int[][] graph, int n) {
        for (int k = 1; k <= n; k++) {
            for (int i = 1; i <= n; i++) {
                for (int j = 1; j <= n; j++) {
                    // INF+INF할 경우, 오버플로우가 발생함 -> 정수 최소값으로 래핑됨
                    // 추가: 두 노드 사이의 경로가 존재할 때만 갱신
                    if (graph[i][k] != INF && graph[k][j] != INF) { 
                        graph[i][j] = Math.min(graph[i][j], graph[i][k] + graph[k][j]); 
                    }
                }
            }
        }
    }

    public static void printGraph(int[][] graph, int n) {
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                if (graph[i][j] == INF) System.out.print(0 + " ");
                else System.out.print(graph[i][j] + " ");
            }
            System.out.println();
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());

        int[][] graph = new int[n + 1][n + 1];

        // 그래프 초기화
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                if (i == j) continue;
                else graph[i][j] = INF;
            }
        }

        StringTokenizer st;
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int v = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());
            int cost = Integer.parseInt(st.nextToken());

            graph[v][w] = cost;
        }

        // 플로이드 워셜 알고리즘 실행
        floyd(graph, n);

        // 결과 출력
        printGraph(graph, n);

        br.close();
    }
}
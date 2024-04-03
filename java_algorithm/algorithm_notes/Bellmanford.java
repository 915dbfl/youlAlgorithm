// 벨만 포드 알고리즘
// 1. 한 노드에서 다른 노드까지의 최단 거리를 구하는 알고리즘
// 2. 간선의 가중치가 음수일 때도 최단 거리를 구할 수 있다.

// 다익스트라와의 차이점
// 1. 음의 가중치가 존재할 경우
    // - 매번 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택하므로 => O(ElogV)
    // - 음수 간선이 존재할 경우 최단 거리를 찾을 수 없음
// 2. 벨만 포드는 매번 모든 간선을 확인한다. => O(VE)
    // - 다익스트라 알고리즘에서의 최적의 해를 항상 포함한다.

// 음의 사이클
// - 한 노드에서 다른 노드까지의 최단 경로는 많아봐야 V-1개의 간선을 지난다는 가정 존재
// - V-1개보다 많은 간선을 지나게 된다면 음의 사이클이 존재한다는 의미이다.

package java_algorithm.algorithm_notes;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.StringTokenizer;
import java.util.Arrays;

public class Bellmanford {
    static ArrayList<Edge> edges;
    static final int INF = Integer.MAX_VALUE;

    static class Edge {
        int v;
        int w;
        int cost;
    
        Edge(int v, int w, int cost) {
            this.v = v;
            this.w = w;
            this.cost = cost;
        }
    }

    public static boolean bellmanFord(int n, int m, int start) {
        int[] dist = new int[n+1];
        Arrays.fill(dist, INF);
        dist[start] = 0;

        // 정점의 개수만큼 반복
        for(int i = 0; i < n; i++) {
            // 간선의 개수만큼 반복
            for(int j = 0; j < m; j++) {
                Edge edge = edges.get(j); // 현재 간선

                // 현재 간선의 들어오는 정점에 대해 비교
                if(dist[edge.v] != INF && dist[edge.w] > dist[edge.v] + edge.cost) {
                    dist[edge.w] = dist[edge.v] + edge.cost;

                    // 음의 순환 존재
                    if(i == n-1) {
                        return false;
                    }
                }
            }
        }
        
        // 출력
        for(int i = 1; i < dist.length; i++) {
            if(dist[i] == INF) {
                System.out.print("INF ");
            } else {
                System.out.print(dist[i] + " ");
            }
        }
        return true;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());

        edges = new ArrayList<>();

        StringTokenizer st;
        for(int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int v = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());
            int cost = Integer.parseInt(st.nextToken());

            edges.add(new Edge(v, w, cost));
        }

        bellmanFord(n, m, 1);

    }
}

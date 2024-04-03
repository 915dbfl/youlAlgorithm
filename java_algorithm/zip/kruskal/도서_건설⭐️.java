package youlAlgorithm.java.zip.kruskal;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.PriorityQueue;

// 최소비용 신장 트리 - 크루스칼 알고리즘

public class 도서_건설 {
    final static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    // 비용 * 건물 = 10^11, long으로 선언해줘야 함.
    static Long total;

    public static void union(int[] parent, int x, int y) {
        x = find(parent, x);
        y = find(parent, y);

        if (x < y) parent[y] = x;
        else parent[x] = y;
    }

    public static int find(int[] parent, int x) {
        if (parent[x] == x) return x;
        else {
            return parent[x] = find(parent, parent[x]);
        }
    }

    public static boolean checkParent(int[] parent) {
        int base = parent[1];
        for(int i = 1; i < parent.length; i++) {
            if(base != find(parent, parent[i])) return false;
        }
        return true;
    }

    public static void kruskal(int[][] graph, int[] parent) {
        Long cost = 0L;

        for(int i = 0; i < graph.length; i++) {
            if (find(parent, graph[i][0]) != find(parent, graph[i][1])) {
                cost += graph[i][2];
                union(parent, graph[i][0], graph[i][1]);
            }
        }
        if(checkParent(parent)) System.out.println(total - cost);
        else System.out.println(-1);
        
    }


    public static void main(String[] args) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[][] graph = new int[m][3];

        total = 0L;
        for(int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            graph[i][0] = Integer.parseInt(st.nextToken());
            graph[i][1] = Integer.parseInt(st.nextToken());
            graph[i][2] = Integer.parseInt(st.nextToken());
            total += graph[i][2];
        }

        // 오름차순으로 정렬
        Arrays.sort(graph, (o1, o2)-> o1[2] - o2[2]);

        int[] parent = new int[n+1];
        for(int i = 0; i <= n; i++) {
            parent[i] = i;
        }

        kruskal(graph, parent);
    }    
}

// 다른 풀이

public class 도서_건설 { 
    static int n, m;
    static ArrayList<Node>[] list;

    static class Node implements Comparable<Node> {
        int to;
        int weight;

        Node(int to, int weight) {
            this.to = to;
            this.weight = weight;
        }

        @Override
        public int compareTo(Node o) {
            return this.weight - o.weight;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        list = new ArrayList[n+1];
        for(int i = 1; i < n+1; i++) {
            list[i] = new ArrayList<>();
        }

        long total = 0;
        int a, b, w;
        for(int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            a = Integer.parseInt(st.nextToken());
            b = Integer.parseInt(st.nextToken());
            w = Integer.parseInt(st.nextToken());

            list[a].add(new Node(b, w));
            list[b].add(new Node(a, w));
            total += w;
        }

        long cost = go();
        System.out.println(cost == -1 ? -1: total - cost);
    }

    public static long go() {
        long sum = 0;
        int cnt = 0;

        boolean[] visited = new boolean[n+1];
        PriorityQueue<Node> queue = new PriorityQueue<>();
        queue.offer(new Node(1, 0));

        while(!queue.isEmpty()) {
            if (cnt == n) break;
            Node now = queue.poll();

            if (visited[now.to]) continue;
            visited[now.to] = true;
            sum += now.weight;
            cnt ++;

            for(Node next: list[now.to]) {
                if (visited[next.to]) continue;
                queue.offer(next);
            }
        }

        return cnt == n ? sum : -1;
    }

}
package java_algorithm.zip.theory;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;
import java.util.ArrayList;

public class 단절점과_단절선 {
    final static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static ArrayList<Integer>[] graph;
    static Edge[] edges;
    static int[] parent;

    static class Edge{
        int start;
        int end;

        Edge(int start, int end) {
            this.start = start;
            this.end = end;
        }
    }

    public static void main(String[] args) throws IOException {
        int n = Integer.parseInt(br.readLine());

        graph = new ArrayList[n+1];
        for(int i = 0; i < n+1; i++) {
            graph[i] = new ArrayList<>();
        }

        StringTokenizer st;
        edges = new Edge[n-1];
        for(int i = 1; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            graph[a].add(b);
            graph[b].add(a);
            edges[i-1] = new Edge(a, b);
        }

        int q = Integer.parseInt(br.readLine());
        for(int i =0 ; i < q; i++) {
            st = new StringTokenizer(br.readLine());
            int t = Integer.parseInt(st.nextToken());
            int k = Integer.parseInt(st.nextToken());

            String res = "yes";
            if (t == 1) {
                if (graph[k].size() <= 1) {
                    res = "no";
                }
            }
            System.out.println(res);
        }

        br.close();
    }
}

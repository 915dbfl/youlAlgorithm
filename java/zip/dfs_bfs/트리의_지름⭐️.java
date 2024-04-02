package youlAlgorithm.java.zip.dfs_bfs;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;

// 모든 정점에서 dfs 진행
// 100000 * 100000 시간초과

public class 트리의_지름 {
    final static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    final static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static ArrayList<Node>[] nodes;
    static boolean[] visited;
    static int max = 0, maxIndex = 0;

    static class Node{
        int end;
        int cost;

        Node(int end, int cost) {
            this.end = end;
            this.cost = cost;
        }

    }

    public static void dfs(int cur, int cost) {
        if (cost > max) {
            maxIndex = cur;
            max = cost;
        }

        for (Node next: nodes[cur]) {
            if(!visited[next.end]) {
                visited[next.end] = true;
                dfs(next.end, cost + next.cost);
                visited[next.end] = false;
            }
        }

    }

    public static void main(String[] args) throws IOException {
        int v = Integer.parseInt(br.readLine());
        nodes = new ArrayList[v+1];

        for(int i = 1; i <= v; i++) {
            nodes[i] = new ArrayList<>();
        }

        // 간선 정보 받아오기
        for(int i = 0; i < v; i++) {
            String[] str = br.readLine().split(" ");
            int start = Integer.parseInt(str[0]);
            for(int j = 1; j < str.length; j = j+2) {
                if (str[j].equals("-1")) break;

                int end = Integer.parseInt(str[j]);
                int cost = Integer.parseInt(str[j+1]);
                nodes[start].add(new Node(end, cost));
            }
        }

        visited = new boolean[v+1];
        visited[1] = true;

        dfs(1, 0);

        visited = new boolean[v+1];
        visited[maxIndex] = true;

        dfs(maxIndex, 0);

        bw.write(String.valueOf(max));
        bw.flush();
        bw.close();
        br.close();
        
    }
}

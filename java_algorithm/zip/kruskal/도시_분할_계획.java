package java_algorithm.zip.kruskal;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.StringTokenizer;
import java.util.Collections;

public class 도시_분할_계획 {
    final static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static ArrayList<Road> roads;
    static int[] parent;

    static class Road implements Comparable<Road> {
        int a;
        int b;
        int c;

        Road(int a, int b, int c) {
            this.a = a;
            this.b = b;
            this.c = c;
        }

        public int compareTo(Road o) {
            return this.c - o.c;
        }
    }

    public static int findParent(int target) {
        if(parent[target] == target) return target;
        else return parent[target] = findParent(parent[target]);
    }

    public static void union(int a, int b) {
        a = findParent(a);
        b = findParent(b);

        if (a < b) parent[b] = a;
        else parent[a] = b;
    }

    public static void main(String[] args) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        roads = new ArrayList<>();
        parent = new int[n+1];
        for(int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());

            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            roads.add(new Road(a, b, c));
        }

        for(int i = 1; i <= n; i++) {
            parent[i] = i;
        }

        // Arrays.sort(roads);
        Collections.sort(roads);

        int ans = 0;
        int max = 0;
        for(int i = 0; i < roads.size(); i++) {
            Road road = roads.get(i);
            if (findParent(road.a) != findParent(road.b)) {
                max = Math.max(max, road.c);
                ans += road.c;
                union(road.a, road.b);
            }
        }

        System.out.println(ans - max);
    }
    
}

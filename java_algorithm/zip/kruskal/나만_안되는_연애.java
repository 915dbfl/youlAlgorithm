package java_algorithm.zip.kruskal;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

// M에서 시작하는 간선을 넣지 않고
// 결국에는 하나의 트리가 만들어져야 하기 때문에
// 단순 크루스칼 알고리즘으로도 풀 수 있음

public class 나만_안되는_연애 {
    final static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static int[] parent;
    static int ans;

    static class Road implements Comparable<Road> {
        int start;
        int end;
        int cost;

        Road(int start, int end, int cost) {
            this.start = start;
            this.end = end;
            this.cost = cost;
        }

        public int compareTo(Road o) {
            return this.cost - o.cost;
        }
    }

    public static int findParent(int target) {
        if(parent[target] == target) return target;
        else return parent[target] = findParent(parent[target]);
    }

    public static void uion(int t1, int t2) {
        t1 = findParent(t1);
        t2 = findParent(t2);

        if (t1 < t2) parent[t2] = t1;
        else parent[t1] = t2;
    }

    public static void main(String[] args) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        String[] school = new String[n+1];
        for(int i = 1; i <= n; i++) {
            school[i] = st.nextToken();
        }

        ArrayList<Road> roads = new ArrayList<>();
        for(int i= 0; i < m; i ++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            int d = Integer.parseInt(st.nextToken());

            roads.add(new Road(u, v, d));
        }

        parent = new int[n+1];
        for(int i = 0; i <= n; i++) {
            parent[i] = i;
        }

        Collections.sort(roads);
        
        for(int i = 0; i < m; i++) {
            int start = roads.get(i).start;
            int end = roads.get(i).end;

            if (!school[start].equals(school[end]) && findParent(start) != findParent(end)) {
                ans += roads.get(i).cost;
                uion(start, end);
            }
        }

        // 모두 동일한 부모를 갖는지 확인
        int baseParet = findParent(1);
        for(int i = 1; i <= n; i++) {
            int tmp = findParent(i);
            if (tmp != baseParet) {
                System.out.println(-1);
                return;
            }
        }

        System.out.println(ans);
        br.close();
        
    }
}

// public class 나만_안되는_연애 {
//     final static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//     static int[] parent;
//     int ans;

//     static class Road implements Comparable<Road> {
//         int start;
//         int end;
//         int cost;

//         Road(int start, int end, int cost) {
//             this.start = start;
//             this.end = end;
//             this.cost = cost;
//         }

//         public int compareTo(Road o) {
//             return this.cost - o.cost;
//         }
//     }

//     public static int findParent(int target) {
//         if(parent[target] == target) return target;
//         else return parent[target] = findParent(parent[target]);
//     }

//     public static void uion(int t1, int t2) {
//         t1 = findParent(t1);
//         t2 = findParent(t2);

//         if (t1 < t2) parent[t2] = t1;
//         else parent[t1] = t2;
//     }

//     public static void main(String[] args) throws IOException {
//         StringTokenizer st = new StringTokenizer(br.readLine());
//         int n = Integer.parseInt(st.nextToken());
//         int m = Integer.parseInt(st.nextToken());

//         st = new StringTokenizer(br.readLine());
//         String[] school = new String[n+1];
//         for(int i = 1; i <= n; i++) {
//             school[i] = st.nextToken();
//         }

//         ArrayList<Road>[] graph = new ArrayList[n+1];
//         for(int i = 0; i <= n; i++) {
//             graph[i] = new ArrayList<>();
//         }

//         for(int i= 0; i < m; i ++) {
//             st = new StringTokenizer(br.readLine());
//             int u = Integer.parseInt(st.nextToken());
//             int v = Integer.parseInt(st.nextToken());
//             int d = Integer.parseInt(st.nextToken());

//             graph[u].add(new Road(u, v, d));
//             graph[v].add(new Road(v, u, d));
//         }

//         parent = new int[n+1];
//         for(int i = 0; i <= n; i++) {
//             parent[i] = i;
//         }

//         // m->m 제외하고 초기 road 큐에 넣기
//         PriorityQueue<Road> que = new PriorityQueue<Road>();
//         for(int i = 1; i <= n; i++) {
//             if(school[i].equals("M")) {
//                 for(Road road: graph[i]) {
//                     if (!school[road.start].equals(school[road.end])) {
//                         que.add(road);
//                     }
//                 }
//             }
//         }

//         int ans = 0;
//         while(!que.isEmpty()) {
//             Road curRoad = que.poll();
            
//             // 부모가 동일하지 않다면 union-find진행
//             if(findParent(curRoad.start) == findParent(curRoad.end)) continue;
//             uion(curRoad.start, curRoad.end);
//             ans += curRoad.cost;

//             // 다음 연결된 자식 확인
//             for(Road road: graph[curRoad.end]) {
//                 // 부모가 갖지 않고, m->m, w->w이 아닐 경우
//                 if (!school[road.start].equals(school[road.end]) && findParent(road.start) != findParent(road.end)) {
//                     que.add(road);
//                 }
//             }
//         }

//         // 모두 동일한 부모를 갖는지 확인
//         int baseParet = findParent(1);
//         for(int i = 1; i <= n; i++) {
//             int tmp = findParent(i);
//             if (tmp != baseParet) {
//                 System.out.println(-1);
//                 return;
//             }
//         }

//         System.out.println(ans);
//         br.close();
        
//     }
// }
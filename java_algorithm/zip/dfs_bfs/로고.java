package java_algorithm.zip.dfs_bfs;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.StringTokenizer;
import java.util.Queue;
import java.util.LinkedList;

// bfs⭐️
// 직사각형을 확인할 때 다음 세 가지 조건만 확인
// 1. a가 b 내포
// 2. b가 a 내포
// 3. a의 밖에 존재

class Rec {
    int x1;
    int y1;
    int x2;
    int y2;
    
    Rec(int x1, int y1, int x2, int y2) {
        this.x1 = x1;
        this.y1 = y1;
        this.x2 = x2;
        this.y2 = y2;
    }
}

public class 로고 {
    static Rec[] map;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int N = Integer.parseInt(br.readLine());
        
        map = new Rec[N+1];
        boolean[] visited = new boolean[N+1];
        
        map[0] = new Rec(0, 0, 0, 0);
        
        for (int i = 1; i <= N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int x1 = Integer.parseInt(st.nextToken());
            int y1 = Integer.parseInt(st.nextToken());
            int x2 = Integer.parseInt(st.nextToken());
            int y2 = Integer.parseInt(st.nextToken());
            map[i] = new Rec(x1, y1, x2, y2);
        }

        int cnt = 0;
        Queue<Integer> q = new LinkedList<>();
        for(int i = 0; i <= N; i++) {
            if(visited[i]) continue;

            visited[i] = true;
            q.add(i);
            
            while(!q.isEmpty()) {
                int cur = q.poll();

                for(int j = 0; j <= N; j++) {
                    if(cur == j || !check(cur, j) || visited[j]) continue;

                    visited[j] = true;
                    q.add(j);
                }
            }

            cnt++;
        }

        System.out.println(cnt-1);
    }

    static boolean check(int cur, int next) {
        Rec c = map[cur];
        Rec n = map[next];

        // 내포하는 경우, 밖에 있는 경우 제외
        if((c.x1 < n.x1 && n.x2 < c.x2 && c.y1 < n.y1 && n.y2 < c.y2)
                || (c.x1 > n.x1 && n.x2 > c.x2 && c.y1 > n.y1 && n.y2 > c.y2) 
                || c.x2 < n.x1 || c.x1 > n.x2 || c.y2 < n.y1 || c.y1 > n.y2 )
            return false;
        
        return true;
    }

}

// union-find 오답

// public class 로고 {
//     final static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//     final static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
//     static ArrayList<Rectangle> recs;

//     static class Rectangle implements Comparable<Rectangle> {
//         int sx;
//         int sy;
//         int ex;
//         int ey;
//         Rectangle parent;

//         Rectangle(int sx, int sy, int ex, int ey) {
//             this.sx = sx;
//             this.sy = sy;
//             this.ex = ex;
//             this.ey = ey;
//             this.parent = this;
//         }

//         public int compareTo(Rectangle o) {
//             if(this.sx >= o.sx) {
//                 if(this.sy >= o.sy) {
//                     return 1;
//                 } else {
//                     return -1;
//                 }
//             } else {
//                 return -1;
//             }
//         }

//     }

//     public static boolean checkXY(Rectangle base, Rectangle target) {
//         if((base.sx < target.sx && target.ex < base.ex && base.sy < target.sy && target.ey < base.ey)
//                 || (base.sx > target.sx && target.ex > base.ex && base.sy > target.sy && target.ey > base.ey) 
//                 || base.ex < target.sx || base.sx > target.ex || base.ey < target.sy || base.sy > target.ey )
//             return false;
        
//         return true;
//     }

//     public static Rectangle findParent(Rectangle target) {
//         if(target.parent == target) {
//             return target.parent;
//         } else {
//             return target.parent = findParent(target.parent);
//         }
//     }

//     public static void unionRectangle(Rectangle cur, Rectangle target) {
//         cur = findParent(cur);
//         target = findParent(target);

//         if (cur.compareTo(target) < 0) {
//             cur.parent = target;
//         } else {
//             target.parent = cur;
//         }
//     }

//     public static void checkTarget(Rectangle target) {
//         // 모든 사각형 확인
//         for(Rectangle curRec: recs) {
//             // 한 붓으로 연결이 가능할 때
//             if (checkXY(curRec, target)) {
//                 unionRectangle(curRec, target);
//             }
//         }

//     }

//     public static void main(String[] args) throws IOException {
//         int n = Integer.parseInt(br.readLine());
//         recs = new ArrayList<>();
//         recs.add(new Rectangle(0, 0, 0, 0));

//         // 사각형 정보 받아오기
//         for(int i = 0; i < n; i++) {
//             int[] info = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
//             recs.add(new Rectangle(info[0], info[1], info[2], info[3]));
//         }

//         // 모든 정사각형 한붓 그리기 확인
//         for(Rectangle curRect: recs) {
//             checkTarget(curRect);
//         }

//         HashSet<Rectangle> parent = new HashSet();
//         for(Rectangle curRect: recs) {
//             parent.add(curRect.parent);
//         }
        
//         bw.write(String.valueOf(parent.size()-1));
//         bw.flush();
//         bw.close();
//         br.close();
        
//     }
// }
package java_algorithm.zip.kruskal;
/*
해설
- 세로 / 가로 1~500
- 석유 크기 측정 -> bfs로 진행
- 매번 석유 크기를 측정한다면? 500 * 250000
- 한번 석유 크기를 측정하고 재활용해야 함 -> union find
*/

import java.util.*;
import java.lang.Math;

class 석유_시추 {
    private static final int[] dx = {-1, 1, 0, 0};
    private static final int[] dy = {0, 0, -1, 1};
    
    private Coordinate[][] parents;
    private Map<Coordinate, Integer> oilSizeMap = new HashMap<>();
    private int height = 0;
    private int width = 0;
    
    private static class Coordinate {
        int x;
        int y;
        
        public Coordinate(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
    
    public int solution(int[][] land) {
        height = land.length;
        width = land[0].length;
        parents = new Coordinate[height][width];
        
        // 모든 오일 사이즈 구하기
        for(int i = 0; i < height; i++) {
            for(int j = 0; j < width; j++) {
                if(land[i][j] == 1 && parents[i][j] == null) {
                    parents[i][j] = new Coordinate(i, j);
                    getOilSize(land, parents[i][j]);
                }
            }
        }
        
        // 시추 진행
        int maxOilSize = 0;
        for(int i = 0; i < width; i++) {
            Set<Coordinate> oilSet = new HashSet<>();
            int oilSize = 0;
            for(int j = 0; j < height; j++) {
                if(parents[j][i] != null) {
                    Coordinate parent = getParent(j, i);
                    if(!oilSet.contains(parent)) {
                        oilSet.add(parent);
                        oilSize += oilSizeMap.getOrDefault(parent, 0);
                    }
                }
            }
            
            maxOilSize = Math.max(maxOilSize, oilSize);
        }
        
        return maxOilSize;
    }
    
    private void getOilSize(int[][] land, Coordinate start) {
        int size = 1;
        ArrayDeque<Coordinate> dq = new ArrayDeque<>();
        dq.add(start);
        
        while(!dq.isEmpty()) {
            Coordinate cur = dq.poll();
            Coordinate curParent = getParent(cur.x, cur.y);
            
            for(int i = 0; i < 4; i++) {
                int nx = cur.x + dx[i];
                int ny = cur.y + dy[i];
                
                if(0 <= nx && nx < height && 0 <= ny && ny < width && land[nx][ny] == 1) {
                    if(parents[nx][ny] != null) continue;
                    
                    Coordinate newCoordi = new Coordinate(nx, ny);
                    parents[nx][ny] = newCoordi;
                    Coordinate nParent = getParent(nx, ny);
                    union(curParent, nParent);
                    size += 1;
                    dq.add(newCoordi);
                }
            }
        }
        
        Coordinate parent = getParent(start.x, start.y);
        oilSizeMap.put(parent, size);
    }
    
    private Coordinate getParent(int x, int y) {
        Coordinate parent = parents[x][y];
        if(parent.x == x && parent.y == y) {
            return parent;
        } else {
            parents[x][y] = getParent(parent.x, parent.y);
            return parents[x][y];
        }
    }
    
    private void union(Coordinate coordi1, Coordinate coordi2) {
        Coordinate p1 = getParent(coordi1.x, coordi1.y);
        Coordinate p2 = getParent(coordi2.x, coordi2.y);
        
        if(p1.x < p2.x || (p1.x == p2.x && p1.y < p2.y)) {
            parents[p2.x][p2.y] = p1;
        } else {
            parents[p1.x][p1.y] = p2;
        }
    }
}
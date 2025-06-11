import java.util.ArrayDeque;
import java.util.Arrays;

class Solution {
    private char[][] board;
    private int height;
    private int width;
    
    private final int[] dx = {-1, 1, 0, 0};
    private final int[] dy = {0, 0, -1, 1};
    
    private static class Coordinate {
        int x;
        int y;
        
        Coordinate(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
    
    public int solution(String[] storage, String[] requests) {
        height = storage.length + 2;
        width = storage[0].length() + 2;
        board = new char[height][width];
        
        // board 채워넣기
        for(int i = 0; i < height; i++) {
            for(int j = 0; j < width; j++) {
                if (i >= 1 && i < height -1 && j >= 1 && j < width -1) {
                    board[i][j] = storage[i-1].charAt(j-1);
                } else {
                    board[i][j] = ' ';
                }
            }
        }
        
        // 방문 초기화
        boolean[][] visited = new boolean[height][width];
        for(int i = 0; i < width; i++) {
            visited[0][i] = true;
            visited[height - 1][i] = true;
        }
        for(int i = 0; i < height; i++) {
            visited[i][0] = true;
            visited[i][width - 1] = true;
        }
        
        
        // 명령어 처리
        int size = requests.length;
        for(int i= 0; i < size; i++) {
            String request = requests[i];
            char target = request.charAt(0);
            
            if (request.length() == 1) {
                bfs(target, visited);
            } else {
                for(int j = 1; j < height - 1; j++) {
                    for(int k = 1; k < width -1; k++) {
                        if(board[j][k] == target) {
                            visited[j][k] = true;
                        }
                    }
                }
            }
        }
        
        int answer = 0;
        for(int i = 1; i < height - 1; i++) {
            for(int j = 1; j < width - 1; j++) {
                if(!visited[i][j]) {
                    answer++;
                }
            }
        }
        
        return answer;
    }
    
    private void bfs(
        char target,
        boolean[][] visited
    ) {
        ArrayDeque<Coordinate> dq = new ArrayDeque<>();
        dq.add(new Coordinate(0, 0));
        boolean[][] memo = new boolean[height][width];
        memo[0][0] = true;
        
        while(!dq.isEmpty()) {
            Coordinate cur = dq.poll();
            
            for(int i = 0; i < 4; i++) {
                int nx = cur.x + dx[i];
                int ny = cur.y + dy[i];
                
                if(!canVisited(nx, ny, memo)) continue;
                
                // 이미 제거된 컨테이너라면 -> 외부 컨테이너로 취급
                if(visited[nx][ny]) {
                    memo[nx][ny] = true;
                    dq.add(new Coordinate(nx, ny));
                // 제거되지 않은 컨테이너라면
                } else if(!visited[nx][ny] && target == board[nx][ny]) {
                    memo[nx][ny] = true;
                    visited[nx][ny] = true;
                }
            }
        }
    }
    
    private boolean canVisited(int nx, int ny, boolean[][] memo) {
        return 0 <= nx && nx < height && 0 <= ny && ny < width && !memo[nx][ny];
    }
}
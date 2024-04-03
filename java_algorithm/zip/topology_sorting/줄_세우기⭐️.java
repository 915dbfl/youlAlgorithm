package youlAlgorithm.java.zip.topology_sorting;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.StringTokenizer;
import java.io.IOException;
import java.util.Queue;

// 위상정렬 - 선후관계 조건이 있는 그래프

public class 줄_세우기 {
    final static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    final static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    public static void main(String[] args) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        // 위상 정렬에 사용할 진입차수 저장 배열
        int[] edgeCount = new int[n+1];
        // 위상 정렬에 사용할 그래프 2차원 리스트
        ArrayList<Integer>[] graph = new ArrayList[n+1];
        for(int i = 0; i <= n; i++) {
            graph[i] = new ArrayList<Integer>();
        }

        // 2차원 리스트의 인덱스가 학생 번호
        // 주어진 키 비교정보에 따라 2차원 정보 초기화
        // 진입차수 배열 값 업데이트
        for(int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            graph[a].add(b);
            edgeCount[b] += 1;
        }

        // 위상 정렬에 사용할 큐
        Queue<Integer> q = new LinkedList();

        // 진입차수가 0인 값 큐에 넣기
        for(int i = 1; i < edgeCount.length; i++) {
            if(edgeCount[i] == 0) {
                q.offer(i);
            }
        }

        while(!q.isEmpty()) {
            int cur = q.poll();

            bw.write(cur + " ");

            // 꺼낸 학생번호의 카 비교한 정보 가져오기
            for(int nxt: graph[cur]) {
                // 해당 학생보다 뒤에 서야하는 학생의 정보 가져오기
                // 뒤에 서야하는 학생의 진입차수 감소
                edgeCount[nxt]--;
                // 감소한 진입차수가 0이면 큐에 학생번호 넣기
                if (edgeCount[nxt] == 0) {
                    q.offer(nxt);
                }
            }
        }

        // 출력
        bw.flush();
    }
}
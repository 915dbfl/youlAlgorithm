package java_algorithm.zip.recursion;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Arrays;

public class 트리의_순회 {
    final static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static int[] inorder;
    static int[] postorder;
    static int[] inorderIdx;

    public static void getTree(int inorderS, int inorderE, int postS, int postE) {
        // root 출력
        int root = postorder[postE];
        System.out.print(root + " ");

        if(postS == postE) return;

        // inorder 안에서 root 위치 파악
        int rootIdx = inorderIdx[postorder[postE]];
        // 왼쪽 트리
        int leftTreeSize = 0;
        if(rootIdx != inorderS) {
            leftTreeSize = rootIdx - inorderS;
            getTree(inorderS, rootIdx - 1, postS, postS +  leftTreeSize - 1);
        }

        // 오른쪽 트리
        if(rootIdx != inorderE) {
            getTree(rootIdx + 1, inorderE, postS +  leftTreeSize, postE-1);
        }
    
    }

    public static void main(String[] args) throws IOException {
        int n = Integer.parseInt(br.readLine());
        inorder = Arrays.stream(br.readLine().split((" "))).mapToInt(Integer::parseInt).toArray();
        postorder = Arrays.stream(br.readLine().split((" "))).mapToInt(Integer::parseInt).toArray();
        inorderIdx = new int[n+1];

        // index 값을 미리 저장해둠
        for(int i = 0; i < n; i++) {
            inorderIdx[inorder[i]] = i;
        }

        getTree(0, n-1, 0, n-1);
    }
}

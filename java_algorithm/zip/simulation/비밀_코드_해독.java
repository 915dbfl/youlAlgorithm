package java_algorithm.zip.simulation;
import java.util.Arrays;
import java.util.Set;
import java.util.stream.Collectors;

public class 비밀_코드_해독 {

    private static final int LENGTH = 5;

    public int solution(int n, int[][] q, int[] ans) {
        return countCombinations(n, 0, new int[LENGTH], q, ans);
    }

    private int countCombinations(
        int n,
        int k,
        int[] currentCombination,
        int[][] q,
        int[] ans
    ) {
        if (k == LENGTH) {
            return isValidCombination(currentCombination, q, ans) ? 1 : 0;
        }

        int count = 0;
        int startNum = (k == 0) ? 1 : currentCombination[k - 1] + 1;

        for (int i = startNum; i <= n - (LENGTH - (k + 1)); i++) {
            currentCombination[k] = i;
            count += countCombinations(n, k + 1, currentCombination, q, ans);
        }
        return count;
    }

    private boolean isValidCombination(
        int[] combi,
        int[][] q,
        int[] ans
    ) {
        Set<Integer> combiSet = Arrays.stream(combi)
                                     .boxed()
                                     .collect(Collectors.toSet());

        for (int index = 0; index < q.length; index++) {
            int[] query = q[index];
            
            int countMatches = 0;
            for (int numInQuery : query) {
                if (combiSet.contains(numInQuery)) {
                    countMatches += 1;
                }
            }
            if (countMatches != ans[index]) {
                return false;
            }
        }
        return true;
    }
}
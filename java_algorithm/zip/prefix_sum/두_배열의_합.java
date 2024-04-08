package java_algorithm.zip.prefix_sum;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Arrays;
import java.util.HashMap;

// 단순 누적합 활용

public class 두_배열의_합 {
    final static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException{
        Long t = Long.parseLong(br.readLine());
        int n = Integer.parseInt(br.readLine());
        long[] aList = Arrays.stream(br.readLine().split(" ")).mapToLong(Long::parseLong).toArray();

        // aList 누적합 구하기: O(1000)
        for(int i = 1; i < n; i++) {
            aList[i] += aList[i-1];
        }

        int m = Integer.parseInt(br.readLine());
        long[] bList = Arrays.stream(br.readLine().split(" ")).mapToLong(Long::parseLong).toArray();

        // bList 누적합 구하기: O(1000)
        for(int i = 1; i < m; i++) {
            bList[i] += bList[i-1];
        }

        HashMap<Long, Long> aMap = new HashMap<>();
        HashMap<Long, Long> bMap = new HashMap<>();

        // 누적합 map 구하기: O(10^6)
        for(int i = 0; i < n; i++) {
            
            if(aMap.containsKey(aList[i])) {
                aMap.put(aList[i], aMap.get(aList[i]) + 1);
            } else{
                aMap.put(aList[i], 1L);
            }

            for (int j = 0; j < i; j++) {
                if(aMap.containsKey(aList[i] - aList[j])) {
                    aMap.put(aList[i] - aList[j], aMap.get(aList[i] - aList[j]) + 1);
                } else{
                    aMap.put(aList[i] - aList[j], 1L);
                }
            }
        }

        // 누적합 map 구하기: O(10^6)
        for(int i = 0; i < m; i++) {
            
            if(bMap.containsKey(bList[i])) {
                bMap.put(bList[i], bMap.get(bList[i]) + 1);
            } else{
                bMap.put(bList[i], 1L);
            }

            for (int j = 0; j < i; j++) {
                if(bMap.containsKey(bList[i] - bList[j])) {
                    bMap.put(bList[i] - bList[j], bMap.get(bList[i] - bList[j]) + 1);
                } else{
                    bMap.put(bList[i] - bList[j], 1L);
                }
            }
        }

        Long ans = 0L;
        for(Long key: bMap.keySet()) {
            if(aMap.keySet().contains(t-key)) {
                ans += bMap.get(key) * aMap.get(t-key);
            }
        }

        System.out.println(ans);
    }
}

// 투포인터 활용

// public class 두_배열의_합 {
//     final static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

//     public static void main(String[] args) throws IOException{
//         Long t = Long.parseLong(br.readLine());
//         int n = Integer.parseInt(br.readLine());
//         long[] aList = Arrays.stream(br.readLine().split(" ")).mapToLong(Long::parseLong).toArray();

//         // aList 누적합 구하기: O(1000)
//         for(int i = 1; i < n; i++) {
//             aList[i] += aList[i-1];
//         }

//         int m = Integer.parseInt(br.readLine());
//         long[] bList = Arrays.stream(br.readLine().split(" ")).mapToLong(Long::parseLong).toArray();

//         // bList 누적합 구하기: O(1000)
//         for(int i = 1; i < m; i++) {
//             bList[i] += bList[i-1];
//         }

//         ArrayList<Long> subA = new ArrayList<>();
//         ArrayList<Long> subB = new ArrayList<>();

//         // 누적합 map 구하기: O(10^6)
//         for(int i = 0; i < n; i++) {
            
//             subA.add(aList[i]);

//             for (int j = 0; j < i; j++) {
//                 subA.add(aList[i] - aList[j]);
//             }
//         }

//         // 누적합 map 구하기: O(10^6)
//         for(int i = 0; i < m; i++) {
            
//             subB.add(bList[i]);

//             for (int j = 0; j < i; j++) {
//                 subB.add(bList[i] - bList[j]);
//             }
//         }

//         Collections.sort(subA);
//         Collections.sort(subB, Comparator.reverseOrder());

//         int p1 = 0;
//         int p2 = 0;
//         long ans = 0;

//         while(p1 < subA.size() && p2 < subB.size()) {
//             long currentA = subA.get(p1);
//             long currentB = subB.get(p2);
//             long sum = currentA + currentB;

//             // t를 만족할 경우
//             if (sum == t) {
//                 long countA = 0;
//                 long countB = 0;
//                 while(p1 < subA.size() && subA.get(p1) == currentA) {
//                     countA++;
//                     p1++;
//                 }

//                 while (p2 < subB.size() && subB.get(p2) == currentB) {
//                     countB++;
//                     p2++;
//                 }

//                 ans += countA * countB;
//             } 
//             // t보다 클 경우
//             else if(sum > t) {
//                 p2 += 1;
//             } 
//             // t보다 작을 경우
//             else {
//                 p1 += 1;
//             }
//         }
//         System.out.println(ans);
//         br.close();
//     }
// }

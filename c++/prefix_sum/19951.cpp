//시간 복잡도를 생각해야 하는 문제

// // 시간초과 - 문제 풀기 전에 시간 복잡도 생각하기
// #include <iostream>
// #include <vector>
// using namespace std;

// int n, m, h;
// vector<int> height;

// int main() {
//     cin >> n >> m;
//     height.assign(n+1, 0);

//     for(int i = 1; i <= n; i++) {
//         cin >> h;
//         height[i] = h;
//     }

//     int a, b, k;
//     // 여기서 시간 복잡도가 n * m -> 100000 * 100000
//     for(int i = 0; i < m; i++) {
//         cin >> a >> b >> k;

//         for(int j = a; j <= b; j++) {
//             height[j] += k;
//         }
//     }

//     for(int k = 1; k <= n; k++) {
//         cout << height[k] << " ";
//     }
// }

// // priority + greater = 최소힙 사용해 풀이
// #include <iostream>
// #include <queue>
// #include <deque>
// #include <vector>
// #include <algorithm>
// using namespace std;

// int n, m, h;
// vector<int> height;
// deque<vector<int>> orders;
// priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;

// int main() {
//     cin >> n >> m;
//     height.assign(n+1, 0);

//     for(int i = 1; i <= n; i++) {
//         cin >> h;
//         height[i] = h;
//     }

//     int a, b, k;
//     for(int i = 0; i < m; i++) {
//         cin >> a >> b >> k;
//         orders.push_back({a, b, k});
//     }

//     sort(orders.begin(), orders.end());
//     // 칸 처음부터 끝까지 돌아가며 최종 높이 구하기
//     int tmp_diff = 0;
//     for (int i = 1; i <= n; i++) {
//         while(!orders.empty() && orders.front()[0] == i) { // 해당 칸에 대한 명령이 존재할 경우
//             tmp_diff += orders.front()[2]; // 명령 diff 추가하기
//             pq.push({orders.front()[1]+1, -orders.front()[2]}); // 해당 명령 diff가 제거될 칸 pq에 저장
//             orders.pop_front(); // 완료된 명령 제거
//         }
//         // 제거될 명령 존재하는지 확인
//         while(!pq.empty() && pq.top().first == i) {
//             tmp_diff += pq.top().second; // 명령 diff 제거
//             pq.pop(); // 제거된 명령 pq에서 pop
//         }

//         // 구해진 최종 diff를 더해 높이 출력
//         cout << height[i] + tmp_diff << " ";
//     }
// }

// best algorithm - 누적합
#include <iostream>
using namespace std;

int n, m, h[100002], a, b, k, o[100001], sum = 0;

int main() {
    ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);

    cin >> n >> m;
    for (int i = 1; i <= n; i++) cin >> h[i];

    for(int i = 0; i < m; i++) {
        cin >> a >> b >> k;
        // 명령을 기록한다. (누적합)
        o[a] += k;
        o[b+1] -= k; 
    }

    for(int i = 1; i <= n; i++) {
        sum += o[i];
        h[i] += sum;
        cout << h[i] << " ";
    }
}